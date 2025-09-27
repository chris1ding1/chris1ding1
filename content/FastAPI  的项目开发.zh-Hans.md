---
title: "Tutorial: Building API Projects with Python FastAPI"
slug: 'tutorial-building-api-projects-with-python-fastapi'
keywords:
  - FastAPI
  - uv
  - API Projects
  - Python
  - uvicorn
  - Tutorial
description: "使用 FastAPI 进行 API 项目开发的简明教程。FastAPI 和本地 Server 的安装，文件夹结构设置、代码编写、数据库连接、质量保证和测试，部署跟维护。"
created: 2025-09-25 16:46:16
updated: 2025-09-27 11:53:20
---

👉 [FastAPI 中文官方教程](https://fastapi.tiangolo.com/zh/learn/)

## 项目创建

创建项目文件夹：

```console
mkdir my-project
cd my-project
```

我们使用 `uv` 来处理虚拟环境、框架安装以及包管理。关于 `uv` 的介绍可自行查看 [uv - Documentation](https://docs.astral.sh/uv/) 和 [uv - Source Code](https://github.com/astral-sh/uv)。

启动虚拟环境 `uv venv --python 3.13`，这将会在你的当前目录下创建一个 .venv 目录。另外，我指定了 Python 版本为 3.13，这是因为当前最新稳定版本为 3.13，并且主流平台对 3.13 版本也进行了支持。如果你还没有安装 Python，可使用 brew 进行安装。

进入到虚拟环境里面 `source .venv/bin/activate`。每次你要安装新包时，都要在这个环境下执行，避免安装的包是不同的 Python 版本安装的。你在开发时，进入后，可以等待今日开发任务完成后再退出。无论安装包还是本地开发、运行，都在此状态下。

`uv` 初始化：`uv init`。这将会给你创建 `main.py` 入口主文件，包管理文件 `pyproject.toml` 文件以及 Python 版本声明文件 `.python-version`。

安装纯净框架：`uv add "fastapi"`。

框架安装完成后，我们在本地开发的时候，需要进行启动以便进行访问和测试，在这里，我们使用 [uvicorn](https://uvicorn.dev/)，安装命令 `uv add 'uvicorn[standard]'`，这里我们使用了 `standard` 版本，而不是纯净版，关于 standard 版本附加的依赖查看 [Installation documentation](https://uvicorn.dev/installation/) 了解更多信息。

如果你是使用 `Git` 进行代码仓库管理，别忘了把 `.venv` 添加到项目根目录下的 `.gitignore` 文件内。对于 `.venv` 目录下的 `.gitignore` 文件，内容设置为 "*"。如果没有 `.venv/.gitignore` 就自己创建下，通常默认就生成了，并且内容为 `*`。

退出虚拟环境 `deactivate`。

## 开发

查看项目当前的文件结构如下（`tree -a -L 1`）：

```
.
├── .git
├── .gitignore
├── .python-version
├── .venv
├── main.py
├── pyproject.toml
├── README.md
└── uv.lock
```

FastAPI 并未像一些框架规定文件夹，但是为了规范以及扩展等方面，我们需要调整文件夹目录结构，每个文件或者文件夹各司其责。如果你是一名成熟的开发者，想必已然想到需要建立哪些文件夹。虽然官方并未规定，但是提供了参考，详情可见 [FastAPI 教程：更大的应用 - 多个文件](https://fastapi.tiangolo.com/zh/tutorial/bigger-applications/)

我们这次要创建的项目，实现写入和查询接口，接口内调用第三方 API 接口，调用个 AWS 服务。数据保存到 PostgreSQL 数据库。

新的结构如下，项目根目录下创建 `app` 目录，原来的入口主文件也移动到  `app` 目录下。`routers` 作为路由文件夹。每个文件夹下创建内容为空的 `__init__.py` 文件，注意，以后每个目录或子目录中都有一个，作用是被用来子包。

```text
.
├── app
│   ├── __init__.py
│   ├── main.py
│   └── routers
│   │   ├── __init__.py
├── .git
├── .gitignore
├── .python-version
├── .venv
├── main.py
├── pyproject.toml
├── README.md
└── uv.lock
```


项目启动，项目根目录下执行：

```bash
uv run uvicorn app.main:app --reload
```

## 部署和维护

包升级：`uv sync --upgrade`
