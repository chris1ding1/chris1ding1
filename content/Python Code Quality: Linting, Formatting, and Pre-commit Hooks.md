---
title: "Python Code Quality: Linting, Formatting, and Pre-commit Hooks"
slug: 'python-code-quality-linting-formatting-and-pre-commit-hooks'
keywords:
  - Python linting
  - Ruff
  - mypy
  - pre-commit
  - code formatting
  - static typing
  - git hooks
  - Python code quality
  - pyproject.toml
description: "Learn how to set up Python code quality tools including Ruff for lightning-fast linting and formatting, mypy for static type checking, and pre-commit for automated git hooks to enforce consistent code standards."
created: 2025-12-09 02:11:10
updated: 2025-12-09 02:31:15
---

## Overview

[Ruff - Astral Docs](https://docs.astral.sh/ruff/) An extremely fast Python linter and code formatter, written in Rust.

[mypy](https://github.com/python/mypy) Optional static typing for Python.

[pre-commit](https://pre-commit.com/) A framework for managing and maintaining multi-language pre-commit hooks. `pre-commit` works for any programming language.

## Installation

```bash
uv add --dev ruff mypy pre-commit
```

```bash
mypy <DIR>
```

```bash
ruff check               # Lint all files in the current directory.
ruff check --fix         # Lint files in the current directory and fix any fixable errors.
ruff check --watch       # Run in watch mode by re-running whenever files change
ruff check path/to/code/ # Lint files in `path/to/code`.
```

```bash
ruff format                   # Format all files in the current directory.
ruff format path/to/code/     # Format all files in `path/to/code` (and any subdirectories).
ruff format path/to/file.py   # Format a single file.
```

Ruff accepts multiple files or directories, separated by spaces.

When running with --fix, Ruff's lint should be placed before Ruff's formatter, and before Black, isort, and other formatting tools, as Ruff's fix behavior can output code changes that require reformatting.

## Configuration

`pyproject.toml`

```toml
[tool.mypy]
strict = true
exclude = [".venv", "venv"]

[tool.ruff]
target-version = "py313"
#exclude = []

[tool.ruff.lint]
select = [
    "E",  # pycodestyle errors
    "W",  # pycodestyle warnings
    "F",  # pyflakes
    "I",  # isort
    "B",  # flake8-bugbear
    "C4",  # flake8-comprehensions
    "UP",  # pyupgrade
    "ARG001", # unused arguments in functions
    "T201",   # print statements are not allowed
]
ignore = [
    "E501",  # line too long, handled by black
    "B008",  # do not perform function calls in argument defaults
    "W191",  # indentation contains tabs
    "B904",  # Allow raising exceptions without from e, for HTTPException
]

[tool.ruff.lint.pyupgrade]
# Preserve types, even if a file imports `from __future__ import annotations`.
keep-runtime-typing = true
```

## pre-commit

`pre-commit --version` should show you what version you're using.

### Add a pre-commit configuration

- create a file named: `.pre-commit-config.yaml`
- you can generate a very basic configuration using `pre-commit sample-config`

Demo:

```yaml
# See https://pre-commit.com for more information
# See https://pre-commit.com/hooks.html for more hooks
repos:
  - repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v6.0.0
    hooks:
      - id: check-added-large-files
      - id: check-toml
      - id: check-yaml
        args:
          - --unsafe
      - id: end-of-file-fixer
      - id: trailing-whitespace
  - repo: https://github.com/charliermarsh/ruff-pre-commit
    rev: v0.14.8
    hooks:
      # Run the linter.
      - id: ruff-check
        args:
          - --fix
      # Run the formatter.
      - id: ruff-format

ci:
  autofix_commit_msg: 🎨 [pre-commit.ci] Auto format from pre-commit.com hooks
  autoupdate_commit_msg: ⬆ [pre-commit.ci] pre-commit autoupdate
```

### Install the git hook scripts

```bash
pre-commit install
```
