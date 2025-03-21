---
title: Linting and Formatting in Vue
keywords:
  - NPM Scripts
  - Nuxt Module
  - Vue
  - ESLint
  - Prettier
  - Linting
  - Formatting
  - Extensions for Visual Studio Code
  - Vite Plugin
description: "Guide to setting up ESLint and Prettier in Vue projects with NPM scripts, Nuxt integration, VS Code extensions, and dev server configuration."
created: 2025-03-21 09:34:03
updated: 2025-03-21 09:34:03
---

## Install

`npm install --save-dev --save-exact prettier`

`npm install --save-dev eslint eslint-plugin-vue typescript-eslint eslint-config-prettier eslint-plugin-prettier`

`npx nuxi module add eslint`

- `eslint-plugin-vue` - Official ESLint plugin for Vue.js
- `typescript-eslint` - Tooling which enables you to use TypeScript with ESLint
- `eslint-config-prettier` - Turns off all rules that are unnecessary or might conflict with Prettier
- `eslint-plugin-prettier` - Runs Prettier as an ESLint rule and reports differences as individual ESLint issues

## ESLint

### NPM Scripts

Add the below to lint commands to your `package.json` script section:

```json
{
  "scripts": {
    "lint": "eslint .",
    "lint:fix": "eslint . --fix",
  },
}
```

- Run the `npm run lint` command to verify code style
- Run the `npm run lint:fix` command to automatically fix issues

### Dev Server Checker

You will need to install extra dependencies vite-plugin-eslint2 for Vite.

```console
npm i -D vite-plugin-eslint2
```

`nuxt.config.ts`

```ts
export default defineNuxtConfig({
  modules: [
    '@nuxt/eslint'
  ],
  eslint: {
    checker: true
  }
})
```

## Extensions for Visual Studio Code

[Vue - Official for VS Code](https://marketplace.visualstudio.com/items?itemName=Vue.volar)

[ESLint for VS Code](https://marketplace.visualstudio.com/items?itemName=dbaeumer.vscode-eslint)

[Prettier - Code formatter for VS Code](https://marketplace.visualstudio.com/items?itemName=esbenp.prettier-vscode)

## See Also

- [ESLint](https://eslint.org/)
- [Prettier](https://prettier.io/)
- [Vue Tooling - Linting](https://vuejs.org/guide/scaling-up/tooling.html#linting)
- [Official ESLint plugin for Vue.js](https://eslint.vuejs.org/)
- [Nuxt ESLint](https://eslint.nuxt.com/packages/module)
- [Why I don't use Prettier](https://antfu.me/posts/why-not-prettier)
