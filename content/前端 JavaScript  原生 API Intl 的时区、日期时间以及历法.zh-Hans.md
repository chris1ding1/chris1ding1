---
title: "JavaScript 原生 API Intl：时区、日期时间与历法"
slug: javascript-yuansheng-api-intl-shiqu-riqishijian-yu-lifa
keywords:
  - JavaScript
  - FE
  - Intl
  - 日历系统
  - 国际日历
  - 日期格式化
  - 时区信息
  - 时区偏移量
  - 每周期的起始星期
description: ""
created: 2026-05-03 14:40:47
updated: 2026-05-03 14:40:47
---

## 格式化实例对象

```javascript
new Intl.DateTimeFormat(locales?, options?)
```

- locales. 必须是 [BCP 47 语言标记](https://tools.ietf.org/html/rfc5646)。不传时，默认为运行环境的语言
- options. 对象格式 `{}`。不传时，各字段默认值

`options`

- `year`: `'numeric'`, `'2-digit'`
- `month`: `'numeric'`, `'2-digit'`, `'long'`, `'short'`, `'narrow'`
- `day`: `'numeric'`, `'2-digit'`
- `weekday`: `'long'`, `'short'`, `'narrow'`
- `hour`: `'numeric'`, `'2-digit'`
- `minute`: `'numeric'`, `'2-digit'`
- `second`: `'numeric'`, `'2-digit'`
- `hour12`: `true`, `false`。默认由 locale 决定
- `timeZone`: IANA 时区标识符，默认为运行环境时区
- `timeZoneName`: `'long'`, `'short'`, `'longOffset'`, `'shortOffset'`
- `calendar`: 日历系统标识符，默认 `'gregory'`

## 时区

### 获取所有支持的时区列表

```javascript
Intl.supportedValuesOf('timeZone')
```

返回时区标识符，数组格式，按字母排序。例如：` ['Africa/Abidjan', 'Africa/Accra', 'Africa/Addis_Ababa', 'Africa/Algiers',...]`。共计 400 多个。

### 获取客户端当前时区

```javascript
Intl.DateTimeFormat().resolvedOptions().timeZone
```

返回字符串 - IANA 时区标识符。例如 `'Asia/Shanghai'`。

### 时区偏移量

指定时区，分别以长短格式输出。

完整格式：

```javascript
new Intl.DateTimeFormat('en', {
  timeZone: 'America/New_York',
  timeZoneName: 'longOffset',
}).formatToParts(new Date())
  .find(p => p.type === 'timeZoneName')?.value

// 'GMT-04:00'
```

短格式：

```javascript
new Intl.DateTimeFormat('en', { 
  timeZone: 'America/New_York',
  timeZoneName: 'shortOffset',
}).formatToParts(new Date())
  .find(p => p.type === 'timeZoneName')?.value

// 'GMT-4'
```

通过 `.replace('GMT', '')` 得到仅偏移量。注意，法语 `fr` 返回的是 `'UTC−04:00'`，阿拉伯语 `ar` 返回的是 `'غرينتش-04:00'`。如果你只为了获得纯粹的偏移量的话，语言可以固定为 `en`。如果不能固定，也可以使用正则提取 `.replace(/^[^+\-\d]+/, '')`。

## 日历系统

### 日历系统标识符

```javascript
Intl.supportedValuesOf('calendar')
```

返回数组格式。例如：`['buddhist', 'chinese', 'coptic', 'dangi', 'ethioaa', 'ethiopic', 'gregory', 'hebrew', 'indian', 'islamic', 'islamic-civil', 'islamic-rgsa', 'islamic-tbla', 'islamic-umalqura', 'iso8601', 'japanese', 'persian', 'roc']`

### 根据日历系统标识符获得本地化名称

```javascript
new Intl.DisplayNames(locales, { type: 'calendar' })
```

参数 locales，可以是字符串的单个语言标识符，例如 `zh-Hans`。也可以是数组格式，例如 `['zh-Hans', 'en-US']`，传数组时，优先用第一个，如果运行时不支持，依次尝试后面的。

```javascript
new Intl.DisplayNames('zh-Hans', { type: 'calendar' }).of('gregory') // '公历'
```

有些日历，在某些语言下，是没有本地化的，会返回标识符本身。

## 获取一周的起始日

不同地区对"一周从哪天开始"的定义不同。根据语言来获得一周的起始日和周末是哪两天。

```javascript
new Intl.Locale(locale).getWeekInfo()
```

执行 `new Intl.Locale('zh-Hans').getWeekInfo()` 返回 `{ firstDay: 1, weekend: [6, 7]}`，意为一周的起始日是星期一，周末是星期六和星期日。

周一为 `1`，以此类推，周日是 `7`。

## 日期时间格式化

### 默认格式的“年月日”

```javascript
new Intl.DateTimeFormat().format(new Date())

// 响应范例：'5/3/2026'
```

### 本地化

```javascript
const nowDate = new Date()

new Intl.DateTimeFormat('zh-Hans', {
  year: 'numeric',
  month: 'long',
  day: '2-digit',
  weekday: 'long',
}).format(nowDate)
// 响应范例：'2026年5月03日星期日'

new Intl.DateTimeFormat('en-US', {
  year: 'numeric',
  month: 'long',
  day: 'numeric',
  weekday: 'long',
}).format(nowDate)
// 响应范例：'Sunday, May 3, 2026'
```

### 结构化响应

以简体中文，结构化，完整的显示年月日。

```javascript
new Intl.DateTimeFormat('zh-Hans', {
  year: 'numeric',
  month: '2-digit',
  day: '2-digit',
}).formatToParts(new Date())
```

**响应范例**

```json
[
    {
        "type": "year",
        "value": "2026"
    },
    {
        "type": "literal",
        "value": "/"
    },
    {
        "type": "month",
        "value": "05"
    },
    {
        "type": "literal",
        "value": "/"
    },
    {
        "type": "day",
        "value": "03"
    }
]
```

### 指定历法

以简体中文，输出“农历”的年月日星期。 

```javascript
new Intl.DateTimeFormat('zh-Hans', {
  calendar: 'chinese',
  year: 'numeric',
  month: 'long',
  day: 'numeric',
  weekday: 'long',
}).format(new Date())
// 响应范例：'2026丙午年三月17星期日'
```