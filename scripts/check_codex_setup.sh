#!/usr/bin/env bash

set -u

required_missing=0

check_command() {
  local command_name="$1"
  local install_hint="$2"

  if command -v "$command_name" >/dev/null 2>&1; then
    printf '[ok] %s: %s\n' "$command_name" "$(command -v "$command_name")"
  else
    printf '[missing] %s\n  install: %s\n' "$command_name" "$install_hint"
    required_missing=1
  fi
}

printf '== Required commands ==\n'
check_command git 'install Git with your operating system package manager'
check_command node 'install Node.js 20.19.0 or newer'
check_command npm 'install npm together with Node.js'
check_command codex 'npm install -g @openai/codex@latest'
check_command openspec 'npm install -g @fission-ai/openspec@1.5.0'
check_command gh 'install GitHub CLI from https://cli.github.com/'

if command -v node >/dev/null 2>&1; then
  node_version="$(node --version)"
  printf '[info] node version: %s\n' "$node_version"
  if ! node -e 'const [a,b]=process.versions.node.split(".").map(Number); process.exit(a>20 || (a===20 && b>=19) ? 0 : 1)'; then
    printf '[error] Node.js must be 20.19.0 or newer for the pinned OpenSpec CLI.\n'
    required_missing=1
  fi
fi

if command -v codex >/dev/null 2>&1; then
  printf '\n== Codex ==\n'
  codex --version || required_missing=1
  if ! codex login status; then
    printf '[action] run: codex login\n'
    required_missing=1
  fi
fi

if command -v openspec >/dev/null 2>&1; then
  printf '\n== OpenSpec ==\n'
  openspec --version || required_missing=1
  openspec list --json || required_missing=1
fi

if command -v gh >/dev/null 2>&1; then
  printf '\n== GitHub authentication ==\n'
  if ! gh auth status; then
    printf '[action] run: gh auth login\n'
    required_missing=1
  fi
fi

printf '\n== Git remotes ==\n'
if git rev-parse --show-toplevel >/dev/null 2>&1; then
  git remote -v
  if ! git remote get-url origin >/dev/null 2>&1; then
    printf '[error] origin is missing; it should point to your personal fork.\n'
    required_missing=1
  fi
  if ! git remote get-url upstream >/dev/null 2>&1; then
    printf '[error] upstream is missing; add TsLouis/smart-grid-ev as upstream.\n'
    required_missing=1
  fi
else
  printf '[error] run this script from inside the smart-grid-ev repository.\n'
  required_missing=1
fi

printf '\n== Optional GitNexus ==\n'
if command -v gitnexus >/dev/null 2>&1; then
  gitnexus --version
  if ! gitnexus status; then
    printf '[action] optional: run gitnexus setup, then gitnexus analyze\n'
  fi
else
  printf '[optional] GitNexus is not installed. Install with: npm install -g gitnexus@1.6.3\n'
fi

if [ "$required_missing" -ne 0 ]; then
  printf '\nSetup is incomplete. Follow the actions above, restart Codex, and run this script again.\n'
  exit 1
fi

printf '\nRequired Codex development setup is ready. Restart Codex after openspec update or MCP changes.\n'
