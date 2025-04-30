---
title: "ARIA 无障碍访问"
slug: ''
keywords:
  - ARIA
  - 无障碍访问
  - A11y
  - 屏幕阅读器
  - Accessibility
  - WAI-ARIA
description: "HTML 无障碍访问属性相关说明。"
created: 2025-03-24 05:22:58
updated: 2025-04-30 01:18:45
---

## 描述

### `aria-label` 和 `aria-labelledby`

`aria-label` 为没有文本内容的元素增加名称，例如只有图标的按钮等。

```html
<button aria-label="搜索">
  <span class="icon-search"></span>
</button>
```

`aria-labelledby` 引用页面上其他的元素内容作为名称信息，值为引用的元素 `id` 值，允许多个，多个的时候以空格隔开，可以包含元素自身的 `id`。在多个的时候屏幕阅读器会按照 id 顺序理解。

```html
<span id="label1">文本助手</span>
<span id="label2">功能：大小写转换、字符统计、单复数转换、大小驼峰、按字母排序、26 个英文字母、标题转换、零宽字符等等</span>
<button aria-labelledby="label1 label2">txtify.app</button>
```

- `aria-labelledby` 的作用与 `aria-label` 相同。它为交互元素提供可识别的无障碍名称。
- 如果一个元素同时设置了这两个属性，那么 `aria-labelledby` 将被使用。`aria-labelledby` 优先于所有其他提供无障碍名称的方法，包括 `aria-label`、`<label>` 和元素的内部文本。

### `aria-describedby` 和 `aria-description`

`aria-describedby`

```html
<button aria-describedby="trash-desc">txtify.app </button>
<p id="trash-desc">
  Items in the trash will be permanently removed after 30 days.
</p>
```

`aria-description`

```html
<div
  aria-label="calendar"
  aria-description="Game schedule for the Boston Red Sox 2021 Season">
  <h1>Red Sox 2021</h1>
  <div role="grid">…</div>
</div>
```

## 控制

`aria-controls` 表达此元素所影响、控制的区域。值为所影响的元素的 ID 值，多个的时候以空格隔开。

```html
<button aria-controls="menu">timego.app 时间伙伴</button>
<div id="menu">
  <p>当前时间</p>
  <p>日历</p>
  <p>时间长度</p>
  <p>倒计时</p>
</div>
```

`aria-expanded="false"` 表示 `aria-controls` 所影响的控件是显示或隐藏。可见时设置为 `true`，不可见时设置为 `false`。

```html
<button aria-expanded="false" aria-controls="widget1">txtify.app 复制 ₿ 字符</button>'
<span class="sr-only">₿ 复制成功</span>
```

```html
<button aria-expanded="true" aria-controls="widget1">txtify.app 复制 ₿ 特殊字符</button>
<span>₿ 复制成功</span>
```

`aria-haspopup` 表示此元素所交互到的元素类型

- false
- true
- menu
- listbox
- tree
- grid
- dialog

## 状态

*`aria-live="..."` 实时区域*

- `aria-live="off"` 在用户主动聚焦到该元素时，屏幕阅读器才会读取其最新内容
- `aria-live="polite"` 非紧急的通知或状态更新
- `aria-live="assertive"` 需要用户立即关注

*`role="..."` 实时区域的角色*

- `role="log"` 聊天、错误、游戏或其他类型的日志
- `role="status"` 适用于表达状态的更新或者实时区域的容器
- `role="alert"` 屏幕闪烁的错误或警告消息
- `role="progressbar"` 进度状态
- `role="marquee"` 滚动的文本，例如股票行情、跑马灯
- `role="timer"` 时钟

*`aria-atomic="true"`* 内容的整体都会被完整宣告

"设定的年份是 1990"

```html
<div id="date-output" role="timer" aria-live="polite" aria-atomic="true">
  设定的年份是：<span id="year-output">1990</span>
</div>
```

- [ARIA: 状态角色](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/status_role)
- [ARIA 实时区域](https://developer.mozilla.org/zh-CN/docs/Web/Accessibility/ARIA/Guides/Live_regions)

## 角色

- role="textbox" 适用于可编辑的非文本输入区域。

## 参考

- [无障碍](https://developer.mozilla.org/zh-CN/docs/Web/Accessibility)
- [ARIA 参考](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference)
- [W3C - WAI-ARIA](https://www.w3.org/WAI/standards-guidelines/aria/)
- [ARIA 设计模式与实践指南](https://www.w3.org/WAI/ARIA/apg/)
