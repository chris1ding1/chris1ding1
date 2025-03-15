---
title: "Fixing Mismatched npm Package Versions: Local vs Registry"
keywords:
  - NPM Package
  - Error
  - Version
  - Install a package
  - View registry info
  - List installed packages
  - aliases
  - Manipulates packages
description: "How to resolve version mismatches between newly installed NPM packages and their remote repository versions?"
created: 2025-03-15 03:42:23
updated: 2025-03-15 03:42:23
---

## List installed packages

```console
npm ls <package>
```

`alias: list`

## View registry info

```console
npm view <package> version
```

`alias: aliases: info, show, v`

## Clears packages cache

```console
npm cache clean --force
```

## Remove a package

```console
npm uninstall <package>
```

`aliases: unlink, remove, rm, r, un`

## Delete node_modules/

```console
rm -rf node_modules/
```

## Delete package-lock.json

```console
rm package-lock.json
```

## Install a package

```console
npm install <package>
```

`aliases: add, i, in, ins, inst, insta, instal, isnt, isnta, isntal, isntall`

## See Also

[npm CLI](https://docs.npmjs.com/cli)
