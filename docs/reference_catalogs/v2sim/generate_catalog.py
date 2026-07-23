"""
V2Sim 代码目录生成器
生成满足 OpenSpec assess-grid-simulation-backends 合同的全字段符号清单。

用法:
    python generate_catalog.py [--pkg-dir <path>] [--output <dir>]

默认从 `pip show v2sim` 自动定位包路径，输出到当前目录。
"""

import ast
import csv
import importlib
import inspect
import os
import sys
import textwrap
from pathlib import Path
from collections import Counter


def find_v2sim_path():
    """自动定位 v2sim 安装路径（不依赖硬编码个人路径）"""
    try:
        import v2sim
        return Path(v2sim.__file__).parent
    except ImportError:
        print("ERROR: v2sim not installed. Run: pip install v2sim==1.4.4")
        sys.exit(1)


def get_visibility(name):
    """判断符号可见性"""
    if name.startswith('__') and name.endswith('__'):
        return 'dunder'
    elif name.startswith('__'):
        return 'private'
    elif name.startswith('_'):
        return 'protected'
    else:
        return 'public'


def get_signature(node):
    """提取函数/方法签名"""
    if not isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
        return ''
    args = []
    all_args = node.args
    # positional args
    for a in all_args.args:
        arg_str = a.arg
        if a.annotation:
            arg_str += ': ' + ast.unparse(a.annotation)
        args.append(arg_str)
    # *args
    if all_args.vararg:
        args.append('*' + all_args.vararg.arg)
    # keyword args
    for a in all_args.kwonlyargs:
        arg_str = a.arg
        if a.annotation:
            arg_str += ': ' + ast.unparse(a.annotation)
        args.append(arg_str)
    # **kwargs
    if all_args.kwarg:
        args.append('**' + all_args.kwarg.arg)
    
    sig = '(' + ', '.join(args) + ')'
    if node.returns:
        sig += ' -> ' + ast.unparse(node.returns)
    return sig


def get_docstring(node):
    """提取 docstring 作为功能说明"""
    doc = ast.get_docstring(node)
    if doc:
        # 取第一行作为摘要
        first_line = doc.strip().split('\n')[0].strip()
        return first_line if first_line else '待人工补充'
    return '待人工补充'


def get_dependencies(node):
    """提取函数体中的外部调用（简化版）"""
    deps = set()
    for child in ast.walk(node):
        if isinstance(child, ast.Attribute):
            if isinstance(child.value, ast.Name):
                deps.add(child.value.id + '.' + child.attr)
    # 限制长度
    dep_list = sorted(deps)[:5]
    return '; '.join(dep_list) if dep_list else ''


def classify_symbol(node, parent_class=None):
    """可靠区分 function / class / method"""
    if isinstance(node, ast.ClassDef):
        return 'class'
    elif isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
        if parent_class:
            return 'method'
        return 'function'
    return 'unknown'


def scan_file(filepath, relpath):
    """扫描单个文件，返回符号列表"""
    symbols = []
    try:
        with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
            source = f.read()
        tree = ast.parse(source)
    except SyntaxError:
        return symbols, True  # parse error

    # 顶层定义
    for node in ast.iter_child_nodes(tree):
        if isinstance(node, ast.ClassDef):
            qualified = relpath.replace('/', '.').replace('.py', '') + '.' + node.name
            symbols.append({
                'file': relpath,
                'qualified_name': qualified,
                'type': 'class',
                'name': node.name,
                'signature': '',
                'visibility': get_visibility(node.name),
                'line': node.lineno,
                'description': get_docstring(node),
                'inputs': '',
                'outputs': '',
                'side_effects': '',
                'dependencies': '',
                'dev_usage': '',
                'evidence_status': 'auto_generated',
                'review_status': 'pending',
            })
            # 类方法
            for item in ast.iter_child_nodes(node):
                if isinstance(item, (ast.FunctionDef, ast.AsyncFunctionDef)):
                    meth_qualified = qualified + '.' + item.name
                    sig = get_signature(item)
                    symbols.append({
                        'file': relpath,
                        'qualified_name': meth_qualified,
                        'type': 'method',
                        'name': item.name,
                        'signature': sig,
                        'visibility': get_visibility(item.name),
                        'line': item.lineno,
                        'description': get_docstring(item),
                        'inputs': sig,
                        'outputs': '',
                        'side_effects': '',
                        'dependencies': get_dependencies(item),
                        'dev_usage': '',
                        'evidence_status': 'auto_generated',
                        'review_status': 'pending',
                    })
        elif isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            qualified = relpath.replace('/', '.').replace('.py', '') + '.' + node.name
            sig = get_signature(node)
            symbols.append({
                'file': relpath,
                'qualified_name': qualified,
                'type': 'function',
                'name': node.name,
                'signature': sig,
                'visibility': get_visibility(node.name),
                'line': node.lineno,
                'description': get_docstring(node),
                'inputs': sig,
                'outputs': '',
                'side_effects': '',
                'dependencies': get_dependencies(node),
                'dev_usage': '',
                'evidence_status': 'auto_generated',
                'review_status': 'pending',
            })

    return symbols, False


def main():
    import argparse
    parser = argparse.ArgumentParser(description='V2Sim code catalog generator')
    parser.add_argument('--pkg-dir', default=None, help='V2Sim package directory')
    parser.add_argument('--output', default='.', help='Output directory')
    args = parser.parse_args()

    pkg_dir = Path(args.pkg_dir) if args.pkg_dir else find_v2sim_path()
    output_dir = Path(args.output)
    output_dir.mkdir(parents=True, exist_ok=True)

    print(f"Scanning: {pkg_dir}")

    all_symbols = []
    files_scanned = 0
    files_failed = 0
    excluded_dirs = {'__pycache__'}

    for root, dirs, files in os.walk(pkg_dir):
        dirs[:] = [d for d in dirs if d not in excluded_dirs]
        for f in files:
            if not f.endswith('.py'):
                continue
            filepath = os.path.join(root, f)
            relpath = os.path.relpath(filepath, pkg_dir).replace('\\', '/')
            symbols, failed = scan_file(filepath, relpath)
            files_scanned += 1
            if failed:
                files_failed += 1
            all_symbols.extend(symbols)

    # 检查重复
    qname_counter = Counter(s['qualified_name'] for s in all_symbols)
    duplicates = {k: v for k, v in qname_counter.items() if v > 1}

    # 去重（保留第一个出现的）
    seen = set()
    unique_symbols = []
    for s in all_symbols:
        if s['qualified_name'] not in seen:
            seen.add(s['qualified_name'])
            unique_symbols.append(s)

    # 写 symbols.csv
    fieldnames = [
        'file', 'qualified_name', 'type', 'name', 'signature',
        'visibility', 'line', 'description', 'inputs', 'outputs',
        'side_effects', 'dependencies', 'dev_usage',
        'evidence_status', 'review_status'
    ]
    csv_path = output_dir / 'symbols.csv'
    with open(csv_path, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(unique_symbols)

    # 统计
    type_counts = Counter(s['type'] for s in unique_symbols)
    desc_empty = sum(1 for s in unique_symbols if s['description'] == '待人工补充')
    desc_filled = len(unique_symbols) - desc_empty

    # 写 coverage.md
    cov_path = output_dir / 'coverage.md'
    with open(cov_path, 'w', encoding='utf-8') as f:
        f.write("# V2Sim 代码目录覆盖率\n\n")
        f.write("## 扫描结果（精确统计）\n\n")
        f.write(f"| 指标 | 值 |\n|------|---|\n")
        f.write(f"| 扫描 .py 文件数 | {files_scanned} |\n")
        f.write(f"| 解析失败文件数 | {files_failed} |\n")
        f.write(f"| 原始符号数（含重复） | {len(all_symbols)} |\n")
        f.write(f"| 去重后唯一符号数 | {len(unique_symbols)} |\n")
        f.write(f"| 重复 qualified_name 数 | {len(duplicates)} |\n")
        f.write(f"| class | {type_counts.get('class', 0)} |\n")
        f.write(f"| function | {type_counts.get('function', 0)} |\n")
        f.write(f"| method | {type_counts.get('method', 0)} |\n")
        f.write(f"| 功能说明已填充 | {desc_filled} |\n")
        f.write(f"| 功能说明待人工补充 | {desc_empty} |\n")
        f.write(f"\n## 排除项\n\n")
        f.write(f"| 排除类型 | 说明 |\n|---------|------|\n")
        f.write(f"| `__pycache__/` | Python 编译缓存 |\n")
        f.write(f"| 非 .py 文件 | 数据文件、配置文件等 |\n")
        f.write(f"| 嵌套定义（二级以下） | 仅扫描顶层和类一级方法 |\n")
        f.write(f"\n## 去重说明\n\n")
        f.write(f"使用 `qualified_name`（模块路径.类名.方法名）作为唯一标识。\n")
        f.write(f"原始扫描发现 {len(duplicates)} 个重复项，已去重保留首次出现。\n")
        if duplicates:
            f.write(f"\n### 重复项示例（前10个）\n\n")
            for i, (k, v) in enumerate(sorted(duplicates.items())[:10]):
                f.write(f"- `{k}` (出现 {v} 次)\n")
        f.write(f"\n## 复核方法\n\n")
        f.write(f"- `evidence_status`: `auto_generated` = 工具自动生成\n")
        f.write(f"- `review_status`: `pending` = 待复核, `reviewed` = 已人工复核\n")
        f.write(f"- 核心模块（core, sim, hub, veh, net, plugins）需逐项人工复核\n")
        f.write(f"- 辅助模块按模块抽检 ≥5 符号\n")

    print(f"\nResults:")
    print(f"  Files scanned: {files_scanned}")
    print(f"  Files failed: {files_failed}")
    print(f"  Unique symbols: {len(unique_symbols)}")
    print(f"  Duplicates removed: {len(all_symbols) - len(unique_symbols)}")
    print(f"  Descriptions filled: {desc_filled}")
    print(f"  Descriptions pending: {desc_empty}")
    print(f"\nOutput:")
    print(f"  {csv_path}")
    print(f"  {cov_path}")


if __name__ == '__main__':
    main()
