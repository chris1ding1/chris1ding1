---
title: "寒假给小孩上的 Python 课"
slug: a-python-programming-course-for-kids-during-the-holidays
keywords:
  - Python
  - 假期学习
  - 编程课
  - 零基础
description: "寒假给零基础的小孩子上的编程课知识点以及总结，Shell 模式的进入退出。打印显示内容，基础的数学运算，数字、字符串、列表的变量定义，列表的切片，if else 语句，查看错误信息等内容。"
created: 2025-02-10 17:03:53
updated: 2025-02-10 17:03:53
---

## 第一节课

主要讲了 Shell 方式的进入、退出，在 Shell 模式里面执行基础数学运算和 `print` 打印。介绍编辑器，了解 python 的扩展名。以及  IDE 和其他一些英文单词。

### Python 的交互模式，Shell 方式

- 如何进入到 Shell 模式？在「终端」或者「命令行窗口」执行 `python`，有时候需要带版本号。
- 成功进入到 Shell 模式？执行 `python` 命令后，看到三个大于号 `>>>`，名为「主提示符」
- 如何从 Shell 模式里面退出？`exit()`,`quit()`，或者快捷键 `Control + d`，快捷键的概念
- 尝试加、减、乘、除、括号，余数计算是 %
- 一行里面多个命令用 `;` 隔开
- `print()` 输出，例子：`print(3)`, `print(4+6)`, `print('ni hao')`

### 编辑器

- 看看编辑器长什么样子，Visual Studio Code，简称 VS Code
- 操作新建文件，保存文件，扩展名主要是 `.py`，可以多种不同的扩展名，例如 `.pyw`，也可以自定义
- 命令行中执行 Python 文件 `python file.py`

### 其他知识点

- IDE 代表集成开发环境
- IDLE（集成开发学习环境） 是 Python 的 IDE
- IDE（integrated development environment）和 IDLE （Integrated Development and Learning Environment）是几个单词的首字母。
- 学习和编辑代码的两种模式：交互模式（也可以称呼为 Shell 窗口、Shell 模式）和编辑器方式，编辑器很常用的有 VS Code 等

了解和学习的一些英文单词发音、英文意义

- python、print、shell、control、exit、quit
- open、file、edit、find、paste、copy、cut、save

## 第二节课

主讲变量的赋值、输出，看错误信息，打印显示内容还有复习之前的内容。告之编程很简单，所见即所得。

### 打印输出

```python
# 会显示 ‘ni hao’
print('ni hao')
# 会显示 ‘234’
print(234)
# 会显示 7
print(3+4)
```

### 变量赋值

`=` 是赋值符号

```python
a=8 # 这就是进行赋值
print(a) # 此时会显示 8
a='bu xi huan' # 这也是赋值，a 会变化，所以称呼为变量
print(a) # 此时会显示 ‘bu xi huan’
```

### 学习查看错误信息

尝试执行以下代码:

```python
print(b)
```

会出现错误信息：

```error
Traceback (most recent call last):
  File "<python-input-0>", line 1, in <module>
    print(a)
          ^
NameError: name 'b' is not defined
```

错误信息的说明

- “Traceback” 代表追踪
- “line 1” 代表第几行出现了错误
- “NameError” 代表具体错误
- “name 'b' is not defined”，这就代表 b 没有定义。

再尝试一个错误

```python
a=abc
print(a) # 此时会报错，因为此时 = 两边都是变量，你没有定义过 abc
```

```python
abc='lll' # 把 lll 赋值给 abc
a=abc # abc 赋值给了 a
print(a) # 此时打印 a 就显示 ‘111’
```

## 第三节课

这节课主要讲的知识点：

- 之前的变量定义，细分的话就是数字类型，字符串类型。
- 编程语言有很多，都是人去定义的，你可以创造自己的编程语言，你设计规则
- 编程是可以通过官网自行学习，[Python3 中文教程文档](https://docs.python.org/zh-cn/3/)，编程所见即所得，多练多敲，熟悉了就好了
- 注释使用 `#` ，'#' 后面跟随的内容，就是注释
- 查看错误信息
- 定义列表类型 `[]`， ，切片操作，索引从 0 开始，
- 列表类型，末尾追加内容使用 `append()`，`end` 的英文释义
- VS Code 是编辑器，还可以通过 `vim` 编辑器打开文件，`q` 指令退出。
- `if else` 语句

定义数字类型

```python
a = 1
```

定义字符串类型，单引号或者双引号包裹起来的内容

```python
a = 'x'
```

### 列表类型

把多个内容放到一起，使用中括号 '[]' 包裹起来，切片显示数据，0 是起始位置

```python
x=['ga', 'zh'] # 把多个内容放到一起，使用中括号 '[]' 包裹起来
print(x) # 显示 ['gao', 'zh']

print(x[0]) # 显示 ‘gao’，输出第一个内容，从 0 开始计算位置
print(x[1]) # 显示 ‘zh’，输出第二个内容，索引位置是 1
```

给列表数据追加内容和倒着输出选定的内容，用负数，起始位置是 -1

```python
x.append('an') # 在末尾追加一个 ‘an’，内容的追加使用 `.append()`
print(x) # 显示 ['gao', 'zh', 'an']
print(x[-1]) # 显示 ‘an’，倒着是负数，起始位置是 -1
```

### if else

通过 `vim` 来打开文件，扩展名是 `.py`，执行 Python 文件的命令是 `python3.11 file.py`

```python
a = 1
b = 2
if b > a:
    print('b 大于 a')
else:
    print('b 不大于 a')
```

文件的执行 `python3.11 file.py`，`3.11` 是版本号。

继续学习查看错误信息：

```python
a = 1
b = 2
if b > a:
    print('b 大于 a')
else
    print('b 不大于 a')
```

执行上面的文件报错如下：

```error
  File ".../file.py", line 5
    else
        ^
SyntaxError: expected ':'
```

- `File` 代表是哪个文件
- `line 5`  代表第几行出现错误
- `SyntaxError: expected ':'` 代表错误信息，原代码中 `else` 后面少跟随了 `:`，补充上 `:` 后，代码正常执行

## 第四节课

待上课，计划讲的内容：

- 复习之前的内容
- 重复变量类型
- 重复注释
- 通过 import 找帮手，进行小数的精确计算，之前询问过
- 如何删除列表内的数据
- `if elseif`
- `for`

## 总结

- 更多的让孩子去敲，孩子们都有好奇心，想尝试什么就让他去尝试，出现错误，就看错误信息，强调查看错误信息的重要性
- 让孩子之间互相提问
- 孩子的上课状态，时间上大概可以在 1 个半小时左右，没什么问题
- 小学三年级以上（含三年级），根据官方文档的节奏系统的学习编程完全没有问题，一方面是有了基本的数学计算，对事务也有了初步的逻辑认知
- 可惜寒假有些短，孩子作业又超多，就只上了四节课
