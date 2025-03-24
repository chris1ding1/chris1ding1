---
title: "Deploy Nuxt Application to Cloudflare"
keywords:
  - Nuxt
  - Cloudflare
  - Serverless
  - Configuration
  - Node Version
  - Nitro App
  - Build Command
  - Deployment
description: "Related configurations and reference documentation for deploying Nuxt to Cloudflare"
created: 2025-03-24 06:57:23
updated: 2025-03-24 07:49:43
---

## Nuxt Configuration

### Route matching

`nuxt.config.ts`

```ts
export default defineNuxtConfig({
  nitro: {
    prerender: {
      autoSubfolderIndex: false
    }
  }
})
```

***Fix Cloudflare 308 Trailing Slash Redirect Issue (`/xxx` to `/xxx/`)***

### Node Version

`touch .nvmrc`

```plaintext
22.14.0
```

## Cloudflare Configuration

> Nuxt can work with third-party content that is not generated or created by Nuxt itself. But sometimes such content can cause problems.
> Accordingly, you should make sure that the following options are unchecked / disabled in Cloudflare. Otherwise, unnecessary re-rendering or hydration errors could impact your production application.

- Speed > Optimization > Content Optimization > Disable "Rocket Loader™"
- Speed > Optimization > Image Optimization > Disable "Mirage"
- Scrape Shield > Disable "Email Address Obfuscation"

> With these settings, you can be sure that Cloudflare won't inject scripts into your Nuxt application that may cause unwanted side effects.

## Cloudflare Build

### Build configuration

***Build command***

To leverage server-side rendering on the edge, set the build command to: `npx nuxt build`.

To statically generate your website, set the build command to: `npx nuxt generate`.

***Build output***

`dist`

## See Also

- [Nuxt · Cloudflare Pages docs](https://developers.cloudflare.com/pages/framework-guides/deploy-a-nuxt-site/)
- [Deployment - CDN Proxy · Get Started with Nuxt](https://nuxt.com/docs/getting-started/deployment#cdn-proxy)
- [Deploy Nitro apps to Cloudflare](https://nitro.build/deploy/providers/cloudflare)
- [Deploy Nuxt to Cloudflare](https://nuxt.com/deploy/cloudflare)
