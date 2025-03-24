---
title: "Nuxt i18n SEO Guide"
keywords:
  - Nuxt
  - Vue
  - i18n
  - SEO
  - Component Interpolation
  - Locale
  - Head
  - Scope resolving
  - link
  - Advanced
  - meta
  - hreflang
  - Basic Usage
  - OpenGraph
  - lang
  - canonical
description: "Basic configuration of Nuxt i18n, SEO, code examples for page components, and related reference documentation."
created: 2025-03-02 08:30:53
updated: 2025-03-24 11:50:07
---

## Configure

`mkdir -p i18n/locales`

`touch i18n/i18n.config.ts i18n/locales/en.json i18n/locales/zh-Hans.json`

`i18n/i18n.config.ts`

```ts
import en from './locales/en.json'
import et from './locales/et.json'

export default defineI18nConfig(() => ({
    legacy: false,
    locale: 'en',
    messages: {
        en,
        et,
    }
}))
```

`nuxt.config.ts`

```ts
export default defineNuxtConfig({
    modules: ['@nuxtjs/i18n'],
    i18n: {
        strategy: 'prefix_except_default',
        defaultLocale: 'en',
        detectBrowserLanguage: false,
        baseUrl: 'https://ex.ex',
        lazy: true,
        locales: [
            {
                code: 'en',
                language: 'en',
                name: 'English',
                file: 'en.json',
            },
            {
                code: 'et',
                language: 'et',
                name: 'Eesti',
                file: 'et.json'
            },
        ],
        vueI18n: 'i18n.config.ts',
    }
})
```

Configuring the vueI18n option can help resolve potential warnings, such as `WARN [Vue warn]: Invalid watch source: en. A watch source must be a getter/effect function, a ref, a reactive object, or an array of these types`. This warning may occur when using certain packages. For example, I encountered it after installing @nuxtjs/sitemap version 7.2.9.

## SEO Documentation examples

### Layout Components Approach

[Nuxt I18n - Setup](https://i18n.nuxtjs.org/docs/guide/seo#setup)

`layouts/default.vue`

```vue
<script setup>
const route = useRoute()
const { t } = useI18n()
const head = useLocaleHead()
const title = computed(() => t(route.meta.title ?? 'TBD', t('layouts.title'))
);
</script>

<template>
  <div>
    <Html :lang="head.htmlAttrs.lang" :dir="head.htmlAttrs.dir">
      <Head>
        <Title>{{ title }}</Title>
        <template v-for="link in head.link" :key="link.hid">
          <Link :id="link.hid" :rel="link.rel" :href="link.href" :hreflang="link.hreflang" />
        </template>
        <template v-for="meta in head.meta" :key="meta.hid">
          <Meta :id="meta.hid" :property="meta.property" :content="meta.content" />
        </template>
      </Head>
      <Body>
        <slot />
      </Body>
    </Html>
  </div>
</template>
```

Access the `baseUrl` result:

```html
<html lang="en" dir="ltr">
  <link id="i18n-alt-en" rel="alternate" href="<i18n.baseUrl>" hreflang="en">
  <link id="i18n-alt-es" rel="alternate" href="<i18n.baseUrl>/es" hreflang="es">
  <link id="i18n-alt-de" rel="alternate" href="<i18n.baseUrl>/de" hreflang="de">
  <link id="i18n-alt-fr" rel="alternate" href="<i18n.baseUrl>/fr" hreflang="fr">
  <link id="i18n-alt-ja" rel="alternate" href="<i18n.baseUrl>/ja" hreflang="ja">
  <link id="i18n-alt-zh" rel="alternate" href="<i18n.baseUrl>/zh-hans" hreflang="zh">
  <link id="i18n-alt-zh-Hans" rel="alternate" href="<i18n.baseUrl>/zh-hans" hreflang="zh-Hans">
  <link id="i18n-xd" rel="alternate" href="<i18n.baseUrl>" hreflang="x-default">
  <link id="i18n-can" rel="canonical" href="<i18n.baseUrl>">
  <meta id="i18n-og-url" content="<i18n.baseUrl>" property="og:url">
  <meta id="i18n-og" content="en" property="og:locale">
  <meta id="i18n-og-alt-es" content="es" property="og:locale:alternate">
  <meta id="i18n-og-alt-de" content="de" property="og:locale:alternate">
  <meta id="i18n-og-alt-fr" content="fr" property="og:locale:alternate">
  <meta id="i18n-og-alt-ja" content="ja" property="og:locale:alternate">
  <meta id="i18n-og-alt-zh-Hans" content="zh_Hans" property="og:locale:alternate">
```

### Composition API Approach

[Nuxt I18n - Feature details](https://i18n.nuxtjs.org/docs/guide/seo#feature-details)

```vue
<script setup>
const i18nHead = useLocaleHead({ seo: { canonicalQueries: ['foo'] } })
useHead(() => ({
  htmlAttrs: {
    lang: i18nHead.value.htmlAttrs!.lang
  },
  link: [...(i18nHead.value.link || [])],
  meta: [...(i18nHead.value.meta || [])]
}))
</script>
```

Access the `baseUrl` result:

```html
<html lang="en">
  <link rel="alternate" href="<i18n.baseUrl>" hreflang="en" data-hid="7fcee50">
  <link rel="alternate" href="<i18n.baseUrl>/es" hreflang="es" data-hid="52a6c69">
  <link rel="alternate" href="<i18n.baseUrl>/de" hreflang="de" data-hid="5d718b2">
  <link rel="alternate" href="<i18n.baseUrl>/fr" hreflang="fr" data-hid="484de76">
  <link rel="alternate" href="<i18n.baseUrl>/ja" hreflang="ja" data-hid="396afb4">
  <link rel="alternate" href="<i18n.baseUrl>/zh-hans" hreflang="zh" data-hid="1a9396e">
  <link rel="alternate" href="<i18n.baseUrl>/zh-hans" hreflang="zh-Hans" data-hid="70511e8">
  <link rel="alternate" href="<i18n.baseUrl>" hreflang="x-default" data-hid="6527e7a">
  <link rel="canonical" href="<i18n.baseUrl>">
  <meta property="og:url" content="<i18n.baseUrl>">
  <meta property="og:locale" content="en">
  <meta property="og:locale:alternate" content="es">
  <meta property="og:locale:alternate" content="de">
  <meta property="og:locale:alternate" content="fr">
  <meta property="og:locale:alternate" content="ja">
  <meta property="og:locale:alternate" content="zh_Hans">
```

## Enhanced Composition API Approach

```vue
<script setup lang="ts">
const i18nHead = useLocaleHead({
    seo: true,
    key: 'id'
});
useHead({
    htmlAttrs: {
        lang: i18nHead.value.htmlAttrs!.lang,
        dir: i18nHead.value.htmlAttrs?.dir
    },
    link: [
        ...(i18nHead.value.link || [])
    ],
    meta: [
        ...(i18nHead.value.meta || [])
    ]
})
</script>
```

Access the `baseUrl` result:

```html
<html lang="en" dir="ltr">
  <link id="i18n-alt-en" rel="alternate" href="<i18n.baseUrl>" hreflang="en">
  <link id="i18n-alt-es" rel="alternate" href="<i18n.baseUrl>/es" hreflang="es">
  <link id="i18n-alt-de" rel="alternate" href="<i18n.baseUrl>/de" hreflang="de">
  <link id="i18n-alt-fr" rel="alternate" href="<i18n.baseUrl>/fr" hreflang="fr">
  <link id="i18n-alt-ja" rel="alternate" href="<i18n.baseUrl>/ja" hreflang="ja">
  <link id="i18n-alt-zh" rel="alternate" href="<i18n.baseUrl>/zh-hans" hreflang="zh">
  <link id="i18n-alt-zh-Hans" rel="alternate" href="<i18n.baseUrl>/zh-hans" hreflang="zh-Hans">
  <link id="i18n-xd" rel="alternate" href="<i18n.baseUrl>" hreflang="x-default">
  <link id="i18n-can" rel="canonical" href="<i18n.baseUrl>">
  <meta id="i18n-og-url" property="og:url" content="<i18n.baseUrl>">
  <meta id="i18n-og" property="og:locale" content="en">
  <meta id="i18n-og-alt-es" property="og:locale:alternate" content="es">
  <meta id="i18n-og-alt-de" property="og:locale:alternate" content="de">
  <meta id="i18n-og-alt-fr" property="og:locale:alternate" content="fr">
  <meta id="i18n-og-alt-ja" property="og:locale:alternate" content="ja">
  <meta id="i18n-og-alt-zh-Hans" property="og:locale:alternate" content="zh_Hans">
```

## Page Component Usage Examples

### Component Interpolation

Sometimes, we need to localize with a locale message that was included in a HTML tag or component. For example:

```html
<p>Powered by <a href="https://1024.dev">1024</a></p>
```

`en.json`

```json
{
    "powered_by": "Powered by {name}"
}
```

```vue
<i18n-t keypath="powered_by" tag="p">
  <template #name>
    <a href="https://1024.dev">
      1024
    </a>
  </template>
</i18n-t>
```

Output:

```html
<p>Powered by <a href="https://1024.dev">1024</a></p>
```

However, You sometimes meet the warning message on your browser console the following:

```text
[intlify] Not found parent scope. use the global scope.
```

A workaround to suppress this warning is to specify global as the scope property of Translation component.

```html
<i18n-t keypath="powered_by" scope="global" tag="p">
  <template #name>
    <a href="https://1024.dev">
      1024
    </a>
  </template>
</i18n-t>
```

## See Also

- [NuxtI18n - Usage](https://i18n.nuxtjs.org/docs/getting-started/usage)
- [useLocaleHead](https://i18n.nuxtjs.org/docs/composables/use-locale-head)
- [API Options](https://i18n.nuxtjs.org/docs/api/options)
- [Vue I18n documentation](https://vue-i18n.intlify.dev/api/general#createi18n)
- [Nuxt 3 integration - Vue I18n](https://vue-i18n.intlify.dev/guide/integrations/nuxt3.html)
- [Component Interpolation | Vue I18n](https://vue-i18n.intlify.dev/guide/advanced/component.html)
