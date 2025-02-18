---
title: "To attach headers to Cloudflare Pages responses"
keywords:
  - Cloudflare
  - Cloudflare Pages
  - Serverless
  - Headers
  - Security configurations
  - CORS
description: "Adding header to Cloudflare Pages: enabling CORS, disabling search engine indexing for pages.dev, and applying security configurations."
created: 2025-02-18T18:29+0800
updated: 2025-02-18T18:29+0800
---

## Create a `_headers` plain text file in the output folder of your project.

```text
[url]
  [name]: [value]
```

## Prevent your pages.dev deployments showing in search results

```text
https://:<Your Project>.pages.dev/*
  X-Robots-Tag: noindex
```

## Cross-Origin Resource Sharing (CORS)

```text
/*
  Access-Control-Allow-Origin: *
```

## Harden security for an application

- `X-Frame-Options: DENY` Prevents your website from being embedded in iframes on other sites. Stops clickjacking attacks.
- `X-Content-Type-Options: nosniff` Forces browsers to strictly use the declared content type. Prevents browsers from guessing file types.
- `Referrer-Policy: no-referrer` Stops sending referrer information to other websites. Enhances user privacy.
- `Permissions-Policy: document-domain=()` Disables document.domain modification. Prevents cross-domain attacks between subdomains.
- `Content-Security-Policy:`
  - `default-src 'self';` Only load resources (images, styles, etc.) from your own domain
  - `script-src 'self';` Only load JavaScript files from your own domain
  - `frame-ancestors 'none';` Block your site from being embedded in iframes anywhere

```text
/*
  X-Frame-Options: DENY
  X-Content-Type-Options: nosniff
  Referrer-Policy: no-referrer
  Permissions-Policy: document-domain=()
  Content-Security-Policy: default-src 'self'; frame-ancestors 'none';
```

[Headers · Cloudflare Pages docs](https://developers.cloudflare.com/pages/configuration/headers/)
