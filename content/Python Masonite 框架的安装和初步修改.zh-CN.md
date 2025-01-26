---
title: Python Masonite 框架的安装和初步修改
slug: python-masonite-install-and-edit
keywords:
  - Python
  - Masonite
  - 教程
  - 项目创建
created: 2025-01-26 15:00:52
updated: 2025-01-26 15:00:52
---

[Masonite 官方文档](https://docs.masoniteproject.com/)

**推荐使用 Python 3.11 版本。更加稳定，不容易出错。**

## 安装和启动

### 创建程序项目目录

```shell
mkdir myapp
cd myapp
```

### 进入虚拟环境

```shell
python3.11 -m venv venv
source venv/bin/activate
```

### 安装 Masonite 依赖包

```shell
pip3.11 install masonite
```

### 生成框架文件

```shell
project start .
project install
```

### Server 启动

```shell
python3.11 craft serve
```

运行后，我得到的访问地址是 `http://127.0.0.1:8000`

## 项目编写

### 创建首页主页控制器

```shell
python3.11 craft controller Home
```

生成文件： `app/controllers/HomeController.py`，默认生成了 `show` 方法和指定了 `welcome` 视图。这不是我们所想要的，并且我们是首页，所以将 `show` 改为 `index`（更符合语义），指定的咱们自己的视图文件，例如 `home`。修改后的代码如下：

```python
from masonite.controllers import Controller
from masonite.views import View


class HomeController(Controller):
    def index(self, view: View):
        return view.render("home")
```

### 创建视图

我们指定了视图 `home`，但是目前并不存在，所以需要进行创建。

```shell
touch templates/home.html
```

`templates/home.html` 文件写一些自己的代码

- `{% extends "base.html" %}` 继承框架生成的基础模版
- `block title` 设定页面标题
- `block content` 内容

```html
{% extends "base.html" %}
{% block title %} Index {% endblock %}

{% block content %}
首页
{% endblock %}
```

### 路由修改

打开 `routes/web.py` 路由文件：

```python
from masonite.routes import Route

ROUTES = [Route.get("/", "WelcomeController@show")]
```

此时，首页根目录指向的还是 `Welcome` 控制器的 `show` 方法。我们要将根目录指向我们的控制器和方法。修改后如下：

```python
from masonite.routes import Route

ROUTES = [Route.get("/", "HomeController@index")]
```

修改完成后，我们访问 `http://127.0.0.1:8000/`，就看到“首页”了。

## 优化和调整

- `templates/welcome.html` 和 `app/controllers/WelcomeController.py` 文件是默认生成"欢迎"控制器和视图，我们用不到，所以进行删除。

- `templates/base.html` 模版里面的 `meta`，加载的 CSS/JS 文件，还有 favicon 文件等等，就根据自己的情况进行修改。

- 在生成环境里面，一定不要使用 `craft serve`。
