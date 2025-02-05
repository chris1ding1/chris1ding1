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
updated: 2025-02-02 09:37:53
---

## 代码编码格式化

- [PHP-CS-Fixer](https://github.com/PHP-CS-Fixer)
- [Laravel Pint](https://laravel.com/docs/11.x/pint)

## 约定

- 控制器名称单数
- 模型名称单数
- 逻辑封装在 `app/Services` 内。每个服务单独的 `xxxService.php` 文件，单数的命名方式
- 视图 view 复数文件夹

## 生产环境的 Composer

### 命令说明

- `--prefer-dist`: 优先使用压缩包下载依赖，下载更快
- `--no-dev`: 不安装开发环境的包（require-dev），只安装生产环境必需的包
- `-o` | `--optimize-autoloader` : 生成优化后的 autoloader，提高类加载速度

```shell
composer install --prefer-dist --no-dev -o
```

## PHPStan 静态检测

[PHPStan 官网](https://phpstan.org/)

### 下载

```shell
composer require --dev phpstan/phpstan
```

### 使用

[命令行参数说明](https://phpstan.org/user-guide/command-line-usage)

- `--level|-l` [规则级别说明](https://phpstan.org/user-guide/rule-levels)
- `--quiet|-q` 静音
- `--configuration|-c` 指定配置文件
- `--error-format` 输出格式。table 默认，json，github。
- `--memory-limit 1G` 使用的内存限制

```shell
vendor/bin/phpstan analyze [-l 级别] [-c 配置文件] <检测路径> [检测路径...]
```

自定义配置文件，项目根目录下创建 `phpstan.neon` 文件，[配置参考](https://phpstan.org/config-reference)

```neon
parameters:
    level: 5
    paths:
        - app
```

将 PHPStan 放到 Composer 中，以便快捷执行。

```json
"scripts": {
    "phpstan": [
        "./vendor/bin/phpstan analyze -c phpstan.neon"
    ]
}
```

添加完成后，可通过 `composer phpstan` 执行。

## 测试框架

- [Pest](https://pestphp.com/)
- [PHPUnit](https://phpunit.de/)

## Laravel

### 文件缓存

一个命令缓存所有文件（配置 config、事件 event、路由 route、视图 view）：

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

## 参考资料

- [Laravel Deployment optimization](https://laravel.com/docs/11.x/deployment)
- [Laravel Best Practices](https://saasykit.com/blog/laravel-best-practices)
