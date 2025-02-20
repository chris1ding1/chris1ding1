---
title: "Complete Guide to Installing Tailwind CSS in Frameworks"
keywords:
  - Tailwind CSS
  - Install
  - Framework Guides
  - Vite
  - Flowbite
  - JavaScript
  - Build
description: "A practical guide for integrating Tailwind CSS in frameworks, with step-by-step instructions for installation, configuration, and common package integrations."
created: 2025-02-20 07:19:18
updated: 2025-02-20 07:19:18
---

A supplement to the official [Tailwind CSS - Installation](https://tailwindcss.com/docs/installation) documentation. Please pay special attention to ensuring your modifications match your framework's directory structure and paths.

## Example framework directory structure

```tree
MyProject
├── node_modules
├── assets
│   ├── css
│   │   └── app.css
│   └── js
│       └── app.js
├── public
│   ├── favicon.ico
│   ├── logo.png
│   ├── robots.txt
│   └── sitemap.xml
├── templates
│   ├── base.html
│   ├── components
│   │   ├── footer.html
│   │   └── nav.html
│   └── index.html
├── package-lock.json
├── package.json
├── vite.config.ts
```

## Create `package` File

Generate `package-lock.json` and `package.json` files. Skip this step if they already exist.

```console
npm init -y
```

## Install Tailwind CSS

```console
npm install tailwindcss @tailwindcss/cli
```

## Import Tailwind CSS

Edit `<YourProject>/assets/css/app.css`

```css
@import "tailwindcss";
@source "../../templates";
```

## Configure `package.json`

*Set `type` to `module`. Add this configuration if you don't have it.*

```json
"type": "module",
"scripts": {
    "build": "vite build",
    "dev": "vite",
  },
```

## Configure Vite Plugin

Edit `vite.config.ts` file.

Notes:

- Make sure to modify the paths for `outDir`, `input`, and `output` to match your project structure
- `emptyOutDir: false`: Prevents clearing your output directory during `npm run` commands. Configure as needed

```ts
import { defineConfig } from 'vite'
import tailwindcss from '@tailwindcss/vite'
import { resolve } from 'path'

export default defineConfig({
  plugins: [
    tailwindcss(),
  ],
  build: {
    outDir: resolve(__dirname, 'public'),
    emptyOutDir: false,
    rollupOptions: {
      input: {
        'css/app': resolve(__dirname, 'assets/css/app.css'),
        'js/app': resolve(__dirname, 'assets/js/app.js')
      },
      output: {
        assetFileNames: '[name].[ext]',
        entryFileNames: '[name].js'
      },
    }
  }
})
```

## Add Flowbite

### Install

```console
npm install flowbite
```

### Import Flowbite CSS

Edit `<YourProject>/assets/css/app.css`

```css
...
@import "flowbite/src/themes/default";
@plugin "flowbite/plugin";
@source "../../node_modules/flowbite";
```

### Import Flowbite JavaScript

Edit `<YourProject>/assets/js/app.js` file.

```javascript
import 'flowbite';
```

## Add other package

Try the `pluralize` package.

```console
npm i pluralize
```

Edit `<YourProject>/assets/js/app.js` file.

```javascript
...
import pluralize from 'pluralize';
window.pluralize = pluralize;
```

After running `npm run dev|build`, you can use functions like `pluralize.singular()` directly in your templates.

## Run

```console
npm run dev
npm run build
```

After execution, `public/css/app.css` and `public/js/app.js` files will be generated. You can now include and load these files in your framework templates. 🎉

## Tips

If you see error hints when opening TypeScript files in your editor, such as missing packages or naming issues, you can install the `@types/node` package to resolve them. This ensures your development environment runs smoothly without any incorrect error notifications, making the development experience more enjoyable. 😄

```console
npm install --save-dev @types/node
```
