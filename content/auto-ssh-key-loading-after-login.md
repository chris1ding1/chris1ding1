---
title: Auto SSH Key Loading After Login
english-title: auto-ssh-key-loading-after-login
created: 2025-01-21
updated: 2025-01-21
---

`vim ~/.ssh/config`

```ssh-config
Host *.github.com
    AddKeysToAgent yes
    IdentityFile <your private key>
```

`vim ~/.bashrc`

```shell
if [ -z "$SSH_AUTH_SOCK" ]; then
    eval "$(ssh-agent -s)"
    ssh-add <your private key>
fi
```
