---
title: "Fixing 500 Internal Server Errors in Nuxt 3 Sessions and Authentication"
slug: 'fixing-500-internal-server-errors-in-nuxt-3-sessions-and-authentication'
keywords:
  - Vue Nuxt
  - AWS Amplify
  - nuxt-auth-utils
  - NUXT_SESSION_PASSWORD
  - Sessions and Authentication
  - 500 Internal Server Error
description: "未进行逻辑变动的 Nuxt 项目，登陆认证接口突然响应了 500 错误，本地测试并没有问题，项目是部署在 AWS Amplify 上。最终是发现 NUXT_SESSION_PASSWORD 配置识别失效，增加配置，问题得以解决。"
created: 2025-09-23 16:49:28
updated: 2025-09-23 16:49:28
---

因网站的认证授权失效了，进行重新登陆，此时发现接口返回了 500。这就有点奇怪了，最近前后端都没有进行任何逻辑变动，只是各自进行了包升级。前端是 Vue Nuxt3，部署在 AWS Amplify。后端是 Python FastAPI，部署在 AWS Lambda 上。

经过一系列检查和调试，最终发现问题是出在 Nuxt 的配置上。无论任何的部署配置，一直都是以安全、稳定的最小化修改，而这个 Nuxt3 项目在 Amplify 上的部署，也是保持此原则。Nuxt 内没有特别的定义，Amplify 的构建设置几乎就是默认的，并且一直都是基于最新的稳定版本 Node22，认证授权一直是 `nuxt-auth-utils` 包，JWT token。在问题发现前，生产环境和本地环境都无问题，也用了一段时间了。而此次发生问题时，在本地调试时是没有问题的。

问题的根本原因是没有识别到 `NUXT_SESSION_PASSWORD` 这个环境变量。在 CloudWatch 日志中看到`[nuxt-auth-utils] NUXT_SESSION_PASSWORD environment variable or runtimeConfig.session.password was not set.` 和 `H3Error: Empty password`。好吧，怪不得，本地测试依然正常。下面，我把整体的核心设置写出来：

Nuxt 的 `nuxt.config.ts` 配置：

```ts
export default defineNuxtConfig({
  compatibilityDate: '2025-07-15',
  modules: ['nuxt-auth-utils'],
  runtimeConfig: {
    session: {
      password: process.env.NUXT_SESSION_PASSWORD,
    },
  },
})
```

AWS Amplify 的构建设置：

```yml
version: 1
frontend:
  phases:
    preBuild:
      commands:
        - 'corepack enable'
        - 'npx --yes nypm install'
    build:
      commands:
        - 'cp .env.example .env'
        - 'sed -i "s/NUXT_SESSION_PASSWORD=/NUXT_SESSION_PASSWORD=${NUXT_SESSION_PASSWORD}/" .env'
        - 'npx nuxt build'
  artifacts:
    baseDirectory: .amplify-hosting
    files:
      - "**/*"
```

注意：AWS Amplify 控制台，托管 - 环境变量，增加 `NUXT_SESSION_PASSWORD`。Nuxt 项目根目录下有 `.env.example` 文件，并且里面有 `NUXT_SESSION_PASSWORD=`。

其它参考资料：

- [nuxt-auth-utils - configuration](https://github.com/atinux/nuxt-auth-utils/tree/main?tab=readme-ov-file#configuration)
- [Nuxt3 - Sessions and Authentication](https://nuxt.com/docs/3.x/guide/recipes/sessions-and-authentication)
- [H3 useSession](https://h3.unjs.io/examples/handle-session)