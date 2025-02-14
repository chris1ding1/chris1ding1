---
title: "寒假给小孩上的 Python 课"
slug: a-python-programming-course-for-kids-during-the-holidays
keywords:
  - Python
  - 假期学习
  - 编程课
  - 零基础
description: "寒假零基础少儿编程课总结，主要讲了 Shell 模式的进入退出，基础的数学运算，数字、字符串、列表的变量定义和打印显示，列表的切片操作，if else 等控制语句，查看错误信息等内容。"
created: 2025-02-10 17:03:53
updated: 2025-02-14 12:57:53
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

### 简要复习

- 如何注释，符号 `#` 后面的内容不会执行，也就是注释，对你的代码添加笔记说明
- 变量赋值，`=` 赋值符号
- 定义数字类型变量，`a=123`
- 定义字符串类型变量，`a='zz'` 或者 `a="cc"`。用单引号或者双引号包裹起来的就是字符串类型
- 定义列表类型，使用中括号包裹起来，`a=['qwe', 23]`，一个变量内存放了多个内容
- 变量的重新赋值，先定义了变量 `a` 为 1，代码也就是 `a=1`。`print(a)` 就会显示出 `1`，接着写代码 `a=2`，那么 `print(a)` 会显示出 2，因为进行了重新赋值
- 查看错误信息
- 列表的索引未，从左到右是从 0 开始，从右往左的话是 -1 开始

#### 注释

```python
# 这是注释，# 符号后面的内容不执行
```

#### 定义数字类型和字符串类型变量

```python
# 这是赋值一个整数类型。
a = 1

# 这是赋值一个字符串类型，字符串用单引号或者引号包裹起来
a = 'gg'
```

#### 重新赋值

```python
a='x' # 定义了一个字符串类型的变量 a
print(a) # print 代表打印，会显示出 x
a='y' # 这就是重新赋值了
print(a) # 再次打印变量 a，会显示 y
```

### 一个错误的例子

```python
a=b
```

报错

```error
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'b' is not defined
```

错误信息中，`NameError: name 'b' is not defined` 代表 b 没有定义。因为 b 在这里被认为是一个变量，但是你从来没有定义过变量 b。

### 列表类型以及追加

```python
a=['bb', 'nn'] # 这就是定义了一个列表类型的变量，可以存放多个内容。这里是存放了 bb 和 nn
print(a) # 显示 ['bb', 'nn']
a.append(3) # 给 a 追加一个内容 3
print(a) # 显示 ['bb', 'nn', 3]
```

### 控制语句 if

```python
a = 1 # 定义一个数字类型变量 a，值是 1
b = 2 # 定义一个数字类型变量 b，值是 2

if a > b:
    print('a 大于 b')
else:
    print('a 不大于 b')
```

### 新内容

#### 找帮手

之前我们碰到过这样的问题，`0.1+0.2` 会得到结果 `0.30000000000000004`。

```python
a = 0.1
b = 0.2
c = a + b
print(c) # 得到不正确的结果 `0.30000000000000004`
```

在很多编程语言里面，小数的计算都是不精确的，所以面对这种情况，就需要找个帮手来帮助我们。

```python
from decimal import Decimal # 从 decimal 工具箱里面使用 Decimal
a = Decimal('0.1') # 你要使用 Decimal 这个帮手，所以要用 Decimal 来定义小数
b = Decimal('0.2')
print(c) # 显示正确结果 0.3
```

### if和elif

```python
a=1
b=1
if a > b # 判断条件 a 大于 b
    print('a 大于 b') # print 里面的内容你可以自定义
elif a == b: # 判断条件 a 是否和 b 相等。两个等于号就是判断是否相等
    print('a 等于 b')
else: # 前面的条件都不满足，就执行下面的代码
    print('a 小于 b')
```

### 如何删除列表内的数据

我们之前学习了给列表类型数据追加内容，有小朋友提问到，如何删除。

```python
a=['gg','aa', 'zz']
a.pop(1) # 删除变量 a 中的 aa，从左往右的索引位置是从 0 开始
print(a) # 打印变量 a，显示 ['gg','zz']
```

## 总结

- 更多的让孩子去敲，孩子们都有好奇心，想尝试什么就让他去尝试，出现错误，就看错误信息，强调查看错误信息的重要性
- 让孩子之间互相提问
- 孩子的上课状态，时间上大概可以在 1 个半小时左右，没什么问题
- 小学三年级以上（含三年级），根据官方文档的节奏系统的学习编程完全没有问题，一方面是有了基本的数学计算，对事务也有了初步的逻辑认知
- 可惜寒假有些短，孩子作业又超多，就只上了四节课
