---
title: "ACME Certs"
keywords:
  - SSL
  - HTTPS
  - Letsencrypt
  - Cert
description: ""
created: 2025-06-08 07:44:14
updated: 2025-06-08 08:07:30
---

## Install

Socat

```console
apt install -y socat
```

Acme

```console
curl https://get.acme.sh | sh
```

## Set

```console
source ~/.bashrc
```

You can also enable auto upgrade

```console
acme.sh --upgrade --auto-upgrade
```

Disable auto upgrade:

```console
acme.sh --upgrade --auto-upgrade 0
```

Default letsencrypt

```console
acme.sh --set-default-ca --server letsencrypt
```

## Cert

Issue

```console
acme.sh --issue -d <DOMAIN> --standalone [--keylength ec-256]
```

Install

```console
acme.sh --install-cert -d <DOMAIN> --ecc \
  --fullchain-file /etc/ssl/private/<DOMAIN>.cer \
  --key-file /etc/ssl/private/<DOMAIN>.key
```

Renew

```console
acme.sh --renew -d example.com
```

## See Also

[acme.sh](https://github.com/acmesh-official/acme.sh)
