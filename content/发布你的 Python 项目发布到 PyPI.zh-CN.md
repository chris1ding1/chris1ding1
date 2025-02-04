---
title: "发布你的 Python 项目到 PyPI"
slug: publish-your-python-package-to-pypi
keywords:
  - PyPI
  - Hatch
  - Build
  - Package
  - Publish
description: "使用 Hatch 工具将 Python 源码发布到 PyPI，Hatch 的下载安装，项目信息配置，编译，命令钩子，以及测试正式环境的发布的具体过程。"
created: 2025-02-04 14:13:09
updated: 2025-02-04 14:13:09
---

## 使用的工具

[Hatch](https://hatch.pypa.io/latest/)

## 安装

```shell
brew install hatch
```

## 项目创建

创建新项目：

```shell
hatch new "Hatch Demo"
```

目录结构

```tree
<Project name>
├── src
│   └── <Project name>
│       ├── __about__.py
│       └── __init__.py
├── tests
│   └── __init__.py
├── LICENSE.txt
├── README.md
└── pyproject.toml
```

已有项目，进入到项目里面，执行：

```shell
hatch new --init
```

源码存放到 `src/<Project name>` 目录下。

## 项目信息修改

一些主要的项目信息修改，`pyproject.toml` 文件。

`project` 块的 `description`,`requires-python`, `keywords` 等信息修改为适合你源码的内容。

```toml
[project]
description = ''
keywords = []
```

依赖项设置，将你的源码所需依赖填写到 `dependencies` 内。

```toml
dependencies = []
```

设置源码路径和需要打包的文件。

参数说明：

- `packages` 你源码的路径
- `include` 可以直接指定文件（`src/...`），也可以指定递归复制指定目录下的所有文件 `{ path = "src"}`

```toml
[tool.hatch.build]
packages = ["src/<你的包名>"]
include = [
    "src/<指定的文件路径>",
    { path = "src/<路径>", recursive = true },
]
```

自定义脚本命令，定义完成后你就可以通过 `<自定义命令名称> <自定义命令的参数>` 执行了。

```toml
[project.scripts]
<自定义命令名称> = "src.<主脚本名称>:<入口函数>"

[tool.hatch.scripts]
<自定义命令的参数> = "python -m <src 下你包名的文件夹名称>.<源码内的文件名称> [方法名字]"
```

设定 Python 版本和开发工具依赖

```toml
[tool.hatch.envs.default]
python = "3.11"
dependencies = [
    "pytest",
    "pytest-cov",
    "black",
    "isort"
]
```

- `hatch run test` 运行测试
- `hatch run format` 运行代码格式化

```toml
[tool.hatch.envs.default.scripts]
test = "pytest tests/ {args}"
format = [
    "black <Dir 1/> [Dir 2]",
    "isort <Dir 1> [Dir 2]"
]
```

## 创建开发环境

```shell
hatch env create
```

## 进入开发环境

```shell
hatch shell
```

退出的的话执行 `exit`。

## 执行你的源码项目命令

```shell
<自定义命令名称> <自定义命令的参数>
```

## 构建

```shell
hatch build
```

### 测试发布

注册 [TestPyPI](https://test.pypi.org/account/register/) 并设置你的 Key。

发布测试版

```shell
hatch publish -r testpypi
```

查看发布的测试结果

```console
open https://test.pypi.org/project/<包名>/
```

下载测试版本（建议进入到虚拟环境中执行）

- `--index-url` 指定主要源为 TestPyPI
- `--extra-index-url` 允许从官方 PyPI 获取依赖

```shell
python3 -m pip install --index-url https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple/ your-package
```

## 正式发布

```shell
hatch publish
```

## 其他命令

- `hatch env remove` 删除环境
- `hatch env show` 查看环境
- `hatch -r` 重载执行
- `hatch clean` 清除旧构建
