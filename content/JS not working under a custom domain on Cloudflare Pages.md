---
title: JS not working under a custom domain on Cloudflare Pages
keywords:
  - Cloudflare
  - Eror
  - website
  - JS/CSS
created: 2025-01-14 13:29:32
updated: 2025-01-14 13:29:32
---

The website loads the CSS styles via `<script src="CDN tailwindcss.js"></script>`, and the request status shows as successful, but the CSS styles are not applied to the website. However, the CSS works correctly on the default domain `*.page.dev`.

I initially asked AI about this issue, and while it provided a lot of information, none of it resolved the problem.

Through a Google search, I found an article titled [Cloudflare Pages - Cloudflare Breaks CSS on Its Own Domain, Works on .pages.dev](https://community.cloudflare.com/t/cloudflare-pages-cloudflare-breaks-css-on-own-domain-works-on-pages-dev/711974). The article mentions turning off 'Auto Minify'.

But I went straight to disabling the 'Speed > Optimization > Content Optimization > Rocket Loader' feature, and immediately after refreshing the site, everything returned to normal.
