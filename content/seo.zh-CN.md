---
title: SEO
keywords:
  - SEO
  - website
created: 2025-01-13 09:42:35
updated: 2025-02-05 06:21:47
---

## 标签元素

### html lang

`<html lang="">`

规范值请查看 [HTML Language Code Reference](https://www.w3schools.com/tags/ref_language_codes.asp)

### title 标题

`<title></title>`

- ahrefs 的建议 "50 - 70 个字符（max 600 pixels）"
- 必应的建议是"不少于 15 个字符"
- [Google 关于标题的最佳实践](https://developers.google.com/search/docs/appearance/title-link)

### meta keywords 关键词

`<meta name="keywords" content="">`

### meta description 描述摘要

`<meta name="description" content="">`

- ahrefs 的建议 "110 到 160 个字符之间"
- [Google 中控制搜索结果中的摘要](https://developers.google.com/search/docs/appearance/snippet)

### 结构化数据 Schema

"网站名称" 的结构化数据格式，简单例子：

```javascript
<script type="application/ld+json">
    {
      "@context" : "https://schema.org",
      "@type" : "WebSite",
      "name" : "网站名称",
      "alternateName" : "别名",
      "url" : "网址"
    }
</script>
```

点击查看 [Google 搜索支持的结构化数据标记](https://developers.google.com/search/docs/appearance/structured-data/search-gallery)，文章、导航、数据集、轮播、课程、数据、论坛、问答、活动、常见问题等等。

添加了结构化数据后，可以通过 [富媒体搜索结果测试 - Google Search Console](https://search.google.com/test/rich-results) 进行测试。

Schema 资料：

- [Schema 数据结构化协议官方文档](https://schema.org/)
- [Schema 架构标记验证器](https://validator.schema.org)

Schema.org 结构化数据标记图片内容的代码例子：

```html
<div itemscope itemtype="https://schema.org/ImageObject">
    <img src="image.jpg" alt="Sample Image" itemprop="contentUrl">
    <meta itemprop="name" content="Sample Image">
    <meta itemprop="description" content="A sample image for demonstration purposes.">
</div>

<div itemscope itemtype="http://schema.org/ImageObject">
  <img itemprop="contentUrl" src="image.jpg" alt="描述">
  <link itemprop="sameAs" href="https://example.com/original-image">
</div>
```

### Open Graph 标签

官网 [Open Graph protocol](https://ogp.me/)

```html
<html prefix="og: https://ogp.me/ns#">
<head>
<title>The Rock (1996)</title>
<meta property="og:title" content="The Rock" />
<meta property="og:type" content="video.movie" />
<meta property="og:url" content="https://www.imdb.com/title/tt0117500/" />
<meta property="og:image" content="https://ia.media-imdb.com/images/rock.jpg" />
...
</head>
...
</html>
```

[Semrush 对 Open Graph 的说明和建议](https://www.semrush.com/blog/open-graph/)

调试器

- [Facebook (meta) 调试器](https://developers.facebook.com/tools/debug/)
- [LinkedIn 分享调试器](https://www.linkedin.com/post-inspector/inspect/)
- TG 缓存刷新机器人 `@WebpageBot`

### Twitter 卡

代码例子可查看 [关于 Twitter (X) Meta 代码例子说明](https://chrisding.xyz/posts/about-twitter-x-cards)

- [Twitter 卡的说明](https://developer.x.com/en/docs/twitter-for-websites/cards/overview/abouts-cards)
- [Twitter 卡官方验证器](https://cards-dev.x.com/validator) `curl -v -A Twitterbot <url>`

### 其他配置

#### robots 机器人爬虫

- index：允许搜索引擎索引（收录）这个页面；相反 noindex
- follow：允许搜索引擎跟踪（爬取）页面上的链接；相反 nofollow

```html
<meta name="robots" content="index, follow" />
```

#### 自适应

```html
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
```

#### `a` 标签的 `ref` 属性

- rel="UGC" 应适用于用户生成的链接。例如，博客评论、论坛帖子
- rel="sponsored" 应适用于广告、赞助、或一些其他补偿协议的链接

```html
<a ref=""></a>
```

注意：关于 X 卡以及 Open Graph，建议使用到的图片存放在网站根目录，并且网站的 TLS 最高版本建议为 1.2，1.2 以上疑似影响效果显示。

## 文件

### 站点地图 sitemap.xml

- [站点地图官方协议](https://www.sitemaps.org/)
- [Google 关于站点地图的说明](https://developers.google.com/search/docs/crawling-indexing/sitemaps/overview)

### robots.txt

- [Google 关于 robots.txt 简介](https://developers.google.com/search/docs/crawling-indexing/robots/intro)
- [允许所有的例子](https://github.com/chris1ding1/config-hub/blob/main/robots.txt)

### IndexNow

- [IndexNow | 必应的说明使用生成](https://www.bing.com/indexnow/getstarted)
- [indexnow 协议官网](https://www.indexnow.org/)

### Favicon icon

- [关于 Google 定义网站图标的说明](https://developers.google.com/search/docs/appearance/favicon-in-search)
- [favicon 生成工具 | RealFavIconGenerator](https://realfavicongenerator.net/)

## 站长平台和平台工具

### 站长工具

- [谷歌站长工具](https://search.google.com/search-console)
- [必应网站管理员工具](https://www.bing.com/webmasters)
- [Yandex](https://webmaster.yandex.com/welcome/)
- [Naver](https://searchadvisor.naver.com/)
- [百度站长](https://ziyuan.baidu.com/site/index)

### SEO 工具

- [Ahrefs.com](https://ahrefs.com)
- [SEMrush](https://www.semrush.com/)
- [SimilarWeb](https://www.similarweb.com/)

### 关键词和趋势工具

- [Google Ads 关键词优化](https://ads.google.com/intl/en_us/home/tools/keyword-planner/)
- [Google Alerts 关键词提醒](https://www.google.com/alerts)
- [Google 趋势指数](https://trends.google.com/trends/)
- [百度指数](https://index.baidu.com/)
- 微信指数

### 文档和其他工具

- [SEO 初学者指南 By ahrefs](https://ahrefs.com/zh/seo)
- [Ahrefs 博客](https://ahrefs.com/blog/zh/)
- [Google 搜索中心 | Google for Developers](https://developers.google.com/search/docs)
- [Bing Webmaster Tools 必应网站站长指南](https://www.bing.com/webmasters/help/webmaster-guidelines-30fba23a)
- [Txtify 文本转换工具 - 用来检测一段文字的字符数量](https://txtify.app/)
- [Merkle SEO hreflang 页面元素和站点地图 标记测试工具](https://technicalseo.com/seo-tools/hreflang/)
- [Aleyda Solis 的 hreflang 页面元素和站点地图 标记生成器工具](https://www.aleydasolis.com/english/international-seo-tools/hreflang-tags-generator/)

### 产品项目提交和推广

完成项目后，可以将项目提交到产品目录网站里。有的平台无条件免费的，也有平台是提交免费，想快速发布的话就要付费，也可以选择数月不等的周期免费发布出来。

- [Indie Voice.app](https://indievoice.app/)
- [Indie hackers](https://www.indiehackers.com/)
- [Product Hunt](https://www.producthunt.com/)
- [Pitch Wall.co](https://pitchwall.co/)
- [uneed](https://www.uneed.best/)
- [betalist](https://betalist.com/)
