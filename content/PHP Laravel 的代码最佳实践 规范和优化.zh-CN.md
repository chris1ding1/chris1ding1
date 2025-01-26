---
title: PHP Laravel 的代码最佳实践 规范和优化
keywords:
  - Laravel
  - 代码优化
  - 代码规范
  - Code
  - 最佳实践
  - PHP
created: 2025-01-26 08:03:46
updated: 2025-01-26 08:03:46
---

## 生产环境的 Composer

### 命令说明

- `--prefer-dist`: 优先使用压缩包下载依赖，下载更快
- `--no-dev`: 不安装开发环境的包（require-dev），只安装生产环境必需的包
- `-o` | `--optimize-autoloader` : 生成优化后的 autoloader，提高类加载速度

```shell
composer install --prefer-dist --no-dev -o
```

## 约定

- 控制器名称单数
- 模型名称单数
- 逻辑封装在 `app/Services` 内。每个服务单独的 `xxxServices.php` 文件，单数的命名方式
- 视图 view 复数文件夹

## Laravel

### 文件缓存

一个命令缓存所有文件（配置 config、事件 event、路由 route、视图 vite）：

```shell
php artisan optimize
```

删除 `optimize` 命令生成的所有缓存文件：

```shell
php artisan optimize:clear
```

删除所有缓存：

```shell
php artisan cache:clear
```

### 模型 Model

`app/Providers/AppServiceProvider.php` 内的 `boot` 方法内增加如下代码：

```php
# 禁止懒加载。N + 1 问题
Model::preventLazyLoading();
# 对于不能处理的属性值赋值时，抛出错误。避免自己的意外疏忽错误。
Model::preventSilentlyDiscardingAttributes();
```

### 代码风格

[Laravel Pint](https://laravel.com/docs/11.x/pint)

## 参考资料

- [Laravel Deployment optimization](https://laravel.com/docs/11.x/deployment)
- [Laravel Best Practices](https://saasykit.com/blog/laravel-best-practices)
