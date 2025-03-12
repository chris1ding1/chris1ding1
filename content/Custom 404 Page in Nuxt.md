---
title: "How to Customize the 404 Page in Nuxt"
keywords:
  - Nuxt
  - 404 Page
  - Error Handling
  - Vue
  - Source code
  - Error Page
description: "Different methods to customize a 404 page in Nuxt, along with relevant resources."
created: 2025-03-12 19:54:50
updated: 2025-03-12 19:54:50
---

- [Nuxt - Error Handling](https://nuxt.com/docs/getting-started/error-handling)
- [Nuxt - Read and edit a live example in Error Handling](https://nuxt.com/docs/examples/advanced/error-handling)
- [Nuxt - error.vue](https://nuxt.com/docs/guide/directory-structure/error)
- [Nuxt - Source code. component nuxt-error-page](https://github.com/nuxt/nuxt/blob/main/packages/nuxt/src/app/components/nuxt-error-page.vue)

## Method 1: Custom 404 Page via Pages Directory

`touch pages/[...404].vue`

## Method 2: Global Error Handling with `error.vue`

`touch layouts/errors/404.vue`

`touch error.vue`

```vue
<template>
    <Error404 v-if="error.statusCode === 404" />
    <NuxtErrorPage v-else :error="error" />
</template>

<script setup lang="ts">
import type { NuxtError } from '#app'
import Error404 from '~/layouts/errors/404.vue'
import NuxtErrorPage from '#app/components/nuxt-error-page.vue'

const props = defineProps({
    error: Object as () => NuxtError
})
</script>
```
