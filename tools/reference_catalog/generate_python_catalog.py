#!/usr/bin/env python3
"""Generate a reproducible function/class/method catalog for a Python package."""

from __future__ import annotations

import argparse
import ast
import csv
import re
from collections import Counter, defaultdict
from dataclasses import dataclass, fields
from pathlib import Path


@dataclass
class Symbol:
    kind: str
    qualified_name: str
    signature: str
    source_anchor: str
    visibility: str
    summary: str
    inputs_outputs: str
    side_effects: str
    dependencies: str
    development_relevance: str
    evidence_status: str
    review_status: str


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--source-root", type=Path, required=True)
    parser.add_argument("--package", required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--project", required=True)
    parser.add_argument("--version", required=True)
    parser.add_argument("--commit", required=True)
    parser.add_argument("--exclude-dir", action="append", default=[])
    parser.add_argument("--manual-review-file", type=Path)
    parser.add_argument("--manual-summary-file", type=Path)
    parser.add_argument("--sampled-module-file", type=Path)
    return parser.parse_args()


def read_policy(path: Path | None) -> set[str]:
    if path is None:
        return set()
    return {
        line.strip()
        for line in path.read_text(encoding="utf-8").splitlines()
        if line.strip() and not line.lstrip().startswith("#")
    }


def read_summaries(path: Path | None) -> dict[str, str]:
    if path is None:
        return {}
    summaries: dict[str, str] = {}
    for line_number, line in enumerate(
        path.read_text(encoding="utf-8").splitlines(), start=1
    ):
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        try:
            qualified_name, summary = line.split("\t", 1)
        except ValueError as error:
            raise ValueError(f"{path}:{line_number}: expected TAB-separated fields") from error
        summaries[qualified_name.strip()] = summary.strip()
    return summaries


def module_name(package: str, relative_path: Path) -> str:
    parts = list(relative_path.with_suffix("").parts)
    if parts[-1] == "__init__":
        parts.pop()
    return ".".join([package, *parts]) if parts else package


def clean_text(value: str) -> str:
    return re.sub(r"\s+", " ", value).strip()


def first_doc_line(node: ast.AST, qualified_name: str) -> str:
    doc = ast.get_docstring(node, clean=True)
    if doc:
        return clean_text(doc.split("\n\n", 1)[0])
    return (
        "待人工补充：源码未提供可直接确认的功能说明；"
        f"需结合 {qualified_name} 的实现与调用链确认。"
    )


def call_name(node: ast.AST) -> str | None:
    if isinstance(node, ast.Name):
        return node.id
    if isinstance(node, ast.Attribute):
        prefix = call_name(node.value)
        return f"{prefix}.{node.attr}" if prefix else node.attr
    return None


def dependencies(node: ast.AST) -> str:
    names = []
    for child in ast.walk(node):
        if isinstance(child, ast.Call):
            name = call_name(child.func)
            if name and name not in names:
                names.append(name)
    return "；".join(names[:16]) if names else "静态扫描未发现直接函数调用"


def side_effects(node: ast.AST) -> str:
    calls = {
        (call_name(child.func) or "").lower()
        for child in ast.walk(node)
        if isinstance(child, ast.Call)
    }
    if any(
        token in name
        for name in calls
        for token in ("open", "write", "save", "dump", "to_json", "to_excel", "to_csv")
    ):
        return "存在文件或序列化读写调用；具体路径和覆盖行为需按调用场景复核"
    if any(
        isinstance(child, (ast.Assign, ast.AugAssign, ast.AnnAssign, ast.Delete))
        and any(isinstance(grandchild, (ast.Attribute, ast.Subscript)) for grandchild in ast.walk(child))
        for child in ast.walk(node)
    ):
        return "可能修改传入对象、网络表或仿真状态；调用前后状态需由适配器校验"
    return "静态扫描未确认外部副作用；运行态副作用仍需在 PoC 中复核"


def signature(node: ast.AST) -> str:
    if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
        prefix = "async " if isinstance(node, ast.AsyncFunctionDef) else ""
        result = f"{prefix}({ast.unparse(node.args)})"
        if node.returns is not None:
            result += f" -> {ast.unparse(node.returns)}"
        return result
    if isinstance(node, ast.ClassDef):
        bases = ", ".join(ast.unparse(base) for base in node.bases)
        return f"class({bases})" if bases else "class"
    return "无法静态解析"


def inputs_outputs(node: ast.AST) -> str:
    if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
        args = [
            arg.arg
            for arg in [
                *node.args.posonlyargs,
                *node.args.args,
                *node.args.kwonlyargs,
            ]
            if arg.arg not in {"self", "cls"}
        ]
        if node.args.vararg:
            args.append(f"*{node.args.vararg.arg}")
        if node.args.kwarg:
            args.append(f"**{node.args.kwarg.arg}")
        output = ast.unparse(node.returns) if node.returns is not None else "返回值未注解"
        return f"输入：{', '.join(args) if args else '无显式输入'}；输出：{output}"
    return "输入：构造参数由 __init__ 或工厂函数定义；输出：类实例"


def relevance(relative_path: Path) -> str:
    value = relative_path.as_posix()
    if any(
        token in value
        for token in (
            "create/",
            "network_schema/",
            "converter/",
            "run.py",
            "pf/",
            "control/",
            "timeseries/",
            "results",
            "auxiliary.py",
        )
    ):
        return "需要适配：可作为新系统数据模型、求解、控制或错误契约的参考"
    if any(token in value for token in ("plotting/", "test/", "diagnostic")):
        return "仅内部参考：不进入首轮后端适配器"
    return "可参考：是否进入适配器边界由后续 PoC 决定"


def review_status(
    qualified_name: str,
    module: str,
    manual_symbols: set[str],
    sampled_modules: set[str],
) -> str:
    if qualified_name in manual_symbols:
        return "人工复核"
    if module in sampled_modules:
        return "抽检通过"
    return "自动生成"


def symbol_from_node(
    node: ast.AST,
    kind: str,
    qualified_name: str,
    relative_path: Path,
    module: str,
    manual_symbols: set[str],
    manual_summaries: dict[str, str],
    sampled_modules: set[str],
) -> Symbol:
    name = qualified_name.rsplit(".", 1)[-1]
    return Symbol(
        kind=kind,
        qualified_name=qualified_name,
        signature=signature(node),
        source_anchor=f"{relative_path.as_posix()}#L{node.lineno}",
        visibility="private" if name.startswith("_") else "public",
        summary=manual_summaries.get(
            qualified_name, first_doc_line(node, qualified_name)
        ),
        inputs_outputs=inputs_outputs(node),
        side_effects=side_effects(node),
        dependencies=dependencies(node),
        development_relevance=relevance(relative_path),
        evidence_status="源码确认（静态 AST）",
        review_status=review_status(
            qualified_name, module, manual_symbols, sampled_modules
        ),
    )


def extract_symbols(
    tree: ast.Module,
    module: str,
    relative_path: Path,
    manual_symbols: set[str],
    manual_summaries: dict[str, str],
    sampled_modules: set[str],
) -> list[Symbol]:
    symbols: list[Symbol] = []
    for node in tree.body:
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            qualified_name = f"{module}.{node.name}"
            symbols.append(
                symbol_from_node(
                    node,
                    "function",
                    qualified_name,
                    relative_path,
                    module,
                    manual_symbols,
                    manual_summaries,
                    sampled_modules,
                )
            )
        elif isinstance(node, ast.ClassDef):
            class_name = f"{module}.{node.name}"
            symbols.append(
                symbol_from_node(
                    node,
                    "class",
                    class_name,
                    relative_path,
                    module,
                    manual_symbols,
                    manual_summaries,
                    sampled_modules,
                )
            )
            for child in node.body:
                if isinstance(child, (ast.FunctionDef, ast.AsyncFunctionDef)):
                    qualified_name = f"{class_name}.{child.name}"
                    symbols.append(
                        symbol_from_node(
                            child,
                            "method",
                            qualified_name,
                            relative_path,
                            module,
                            manual_symbols,
                            manual_summaries,
                            sampled_modules,
                        )
                    )
    return symbols


def markdown_cell(value: str) -> str:
    return clean_text(value).replace("|", "\\|")


def write_module_catalog(path: Path, module: str, symbols: list[Symbol]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    columns = [
        "kind",
        "qualified_name",
        "signature",
        "source_anchor",
        "summary",
        "inputs_outputs",
        "side_effects",
        "dependencies",
        "development_relevance",
        "evidence_status",
        "review_status",
    ]
    lines = [
        f"# `{module}`",
        "",
        f"本模块共记录 {len(symbols)} 个函数、类或方法。",
        "",
        "| " + " | ".join(columns) + " |",
        "| " + " | ".join("---" for _ in columns) + " |",
    ]
    for symbol in symbols:
        values = [markdown_cell(str(getattr(symbol, column))) for column in columns]
        lines.append("| " + " | ".join(values) + " |")
    lines.append("")
    path.write_text("\n".join(lines), encoding="utf-8")


def merge_duplicate_symbols(symbols: list[Symbol]) -> tuple[list[Symbol], list[str]]:
    grouped: dict[str, list[Symbol]] = defaultdict(list)
    for symbol in symbols:
        grouped[symbol.qualified_name].append(symbol)

    merged: list[Symbol] = []
    coalesced: list[str] = []
    review_priority = {"自动生成": 0, "抽检通过": 1, "人工复核": 2}
    for qualified_name, definitions in grouped.items():
        if len(definitions) == 1:
            merged.append(definitions[0])
            continue
        coalesced.append(qualified_name)
        first = definitions[0]
        first.signature = "；".join(dict.fromkeys(item.signature for item in definitions))
        first.source_anchor = "；".join(
            dict.fromkeys(item.source_anchor for item in definitions)
        )
        first.summary = "；".join(dict.fromkeys(item.summary for item in definitions))
        first.inputs_outputs = "；".join(
            dict.fromkeys(item.inputs_outputs for item in definitions)
        )
        first.side_effects = "；".join(
            dict.fromkeys(item.side_effects for item in definitions)
        )
        first.dependencies = "；".join(
            dict.fromkeys(item.dependencies for item in definitions)
        )
        first.review_status = max(
            (item.review_status for item in definitions),
            key=review_priority.__getitem__,
        )
        merged.append(first)
    return sorted(merged, key=lambda item: item.qualified_name), sorted(coalesced)


def main() -> None:
    args = parse_args()
    package_root = args.source_root / args.package
    output = args.output
    excluded = set(args.exclude_dir)
    manual_symbols = read_policy(args.manual_review_file)
    manual_summaries = read_summaries(args.manual_summary_file)
    sampled_modules = read_policy(args.sampled_module_file)

    output.mkdir(parents=True, exist_ok=True)
    module_output = output / "modules"
    module_output.mkdir(parents=True, exist_ok=True)

    source_files: list[Path] = []
    excluded_files: list[Path] = []
    for path in sorted(package_root.rglob("*.py")):
        relative_to_package = path.relative_to(package_root)
        if any(part in excluded for part in relative_to_package.parts):
            excluded_files.append(path)
        else:
            source_files.append(path)

    all_symbols: list[Symbol] = []
    module_symbols: dict[tuple[Path, str], list[Symbol]] = defaultdict(list)
    parse_errors: list[tuple[Path, str]] = []

    for path in source_files:
        relative_to_package = path.relative_to(package_root)
        relative_to_root = path.relative_to(args.source_root)
        module = module_name(args.package, relative_to_package)
        try:
            tree = ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
        except (SyntaxError, UnicodeDecodeError) as error:
            parse_errors.append((relative_to_root, str(error)))
            continue
        symbols = extract_symbols(
            tree,
            module,
            relative_to_root,
            manual_symbols,
            manual_summaries,
            sampled_modules,
        )
        all_symbols.extend(symbols)
        module_symbols[(relative_to_package, module)].extend(symbols)

    all_symbols, coalesced_definitions = merge_duplicate_symbols(all_symbols)
    fieldnames = [field.name for field in fields(Symbol)]
    with (output / "symbols.csv").open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        for symbol in all_symbols:
            writer.writerow(vars(symbol))

    for (relative_path, module), symbols in module_symbols.items():
        symbols, _ = merge_duplicate_symbols(symbols)
        target = module_output / relative_path.with_suffix(".md")
        write_module_catalog(target, module, symbols)

    counts = Counter(symbol.kind for symbol in all_symbols)
    review_counts = Counter(symbol.review_status for symbol in all_symbols)
    names = Counter(symbol.qualified_name for symbol in all_symbols)
    duplicates = sorted(name for name, count in names.items() if count > 1)
    missing_manual = sorted(manual_symbols - set(names))
    missing_summaries = sorted(manual_symbols - set(manual_summaries))
    empty_summaries = [
        symbol.qualified_name for symbol in all_symbols if not symbol.summary.strip()
    ]

    coverage_lines = [
        "# 覆盖率与完整性报告",
        "",
        f"- 项目：`{args.project}`",
        f"- 固定版本：`{args.version}`",
        f"- 固定提交：`{args.commit}`",
        f"- 扫描根目录：`{args.package}/`",
        f"- 已解析生产源码文件：{len(source_files) - len(parse_errors)}",
        f"- 解析失败文件：{len(parse_errors)}",
        f"- 排除 Python 文件：{len(excluded_files)}",
        f"- 符号总数：{len(all_symbols)}",
        f"- 函数：{counts['function']}",
        f"- 类：{counts['class']}",
        f"- 方法：{counts['method']}",
        f"- 人工复核：{review_counts['人工复核']}",
        f"- 模块抽检：{review_counts['抽检通过']}",
        f"- 自动生成：{review_counts['自动生成']}",
        f"- 空功能说明：{len(empty_summaries)}",
        f"- 重复限定名：{len(duplicates)}",
        f"- 已合并的多处定义：{len(coalesced_definitions)}",
        f"- 人工复核策略中未找到的符号：{len(missing_manual)}",
        f"- 人工复核符号缺少人工摘要：{len(missing_summaries)}",
        "",
        "## 排除规则",
        "",
        "- 排除目录：" + (", ".join(f"`{item}`" for item in sorted(excluded)) or "无"),
        "- 测试、示例、vendored、生成代码和构建产物仅在明确命中上述目录时排除。",
        "",
        "## 完整性判定",
        "",
        f"- 可解析源码限定名与目录限定名集合：{'一致' if not duplicates else '存在重复'}。",
        f"- 所有符号功能说明非空：{'是' if not empty_summaries else '否'}。",
        f"- 人工复核策略中的符号均被扫描：{'是' if not missing_manual else '否'}。",
        "",
        "## 解析失败",
        "",
    ]
    if args.project == "pandapower":
        coverage_lines.insert(
            coverage_lines.index("## 完整性判定") - 1,
            "- `pypower/` 是 pandapower 运行时求解链的一部分，本次未作为 vendored 代码排除。",
        )
    if parse_errors:
        coverage_lines.extend(
            f"- `{path.as_posix()}`：{clean_text(error)}"
            for path, error in parse_errors
        )
    else:
        coverage_lines.append("- 无。")
    coverage_lines.extend(["", "## 重复限定名", ""])
    coverage_lines.extend(f"- `{name}`" for name in duplicates)
    if not duplicates:
        coverage_lines.append("- 无。")
    coverage_lines.extend(["", "## 已合并的多处定义", ""])
    coverage_lines.extend(
        f"- `{name}`：同一运行时限定名的 getter/setter、兼容分支或重定义已合并，源码锚点全部保留。"
        for name in coalesced_definitions
    )
    if not coalesced_definitions:
        coverage_lines.append("- 无。")
    coverage_lines.extend(["", "## 未命中的人工复核符号", ""])
    coverage_lines.extend(f"- `{name}`" for name in missing_manual)
    if not missing_manual:
        coverage_lines.append("- 无。")
    coverage_lines.extend(["", "## 缺少人工摘要的复核符号", ""])
    coverage_lines.extend(f"- `{name}`" for name in missing_summaries)
    if not missing_summaries:
        coverage_lines.append("- 无。")
    coverage_lines.append("")
    (output / "coverage.md").write_text(
        "\n".join(coverage_lines), encoding="utf-8"
    )

    print(
        f"files={len(source_files) - len(parse_errors)} "
        f"symbols={len(all_symbols)} duplicates={len(duplicates)} "
        f"empty_summaries={len(empty_summaries)} parse_errors={len(parse_errors)}"
    )
    if (
        parse_errors
        or duplicates
        or empty_summaries
        or missing_manual
        or missing_summaries
    ):
        raise SystemExit(1)


if __name__ == "__main__":
    main()
