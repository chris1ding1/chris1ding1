---
title: "Linux firewall command ufw"
slug: 'linux-firewall-command-ufw'
keywords:
  - UFW Essentials
  - Firewall Rules
  - Linux
description: "Linux firewall command ufw"
created: 2025-06-03 02:58:15
updated: 2025-06-03 02:58:15
---

`ufw --help`

Example Output:

```plaintext
Usage: ufw COMMAND

Commands:
 enable                          enables the firewall
 disable                         disables the firewall
 default ARG                     set default policy
 logging LEVEL                   set logging to LEVEL
 allow ARGS                      add allow rule
 deny ARGS                       add deny rule
 reject ARGS                     add reject rule
 limit ARGS                      add limit rule
 delete RULE|NUM                 delete RULE
 insert NUM RULE                 insert RULE at NUM
 prepend RULE                    prepend RULE
 route RULE                      add route RULE
 route delete RULE|NUM           delete route RULE
 route insert NUM RULE           insert route RULE at NUM
 reload                          reload firewall
 reset                           reset firewall
 status                          show firewall status
 status numbered                 show firewall status as numbered list of RULES
 status verbose                  show verbose firewall status
 show ARG                        show firewall report
 version                         display version information

Application profile commands:
 app list                        list application profiles
 app info PROFILE                show information on PROFILE
 app update PROFILE              update PROFILE
 app default ARG                 set default application policy
```

`sudo ufw status`

Shows the rules in a simple format, listing the allowed or denied ports, protocols, source/destination, displays the current status of the ufw firewall, including whether it is active or inactive and a list of enabled firewall rules.

Example Output:

```plaintext
Status: active

To                         Action      From
--                         ------      ----
22                         ALLOW       Anywhere
443                        ALLOW       Anywhere
```

`sudo ufw status numbered`

Similar to ufw status, but each rule is prefixed with a number, making it easier to reference specific rules when modifying or deleting them (e.g., with `ufw delete <number>`).

Example Output:

```plaintext
Status: active

     To                         Action      From
     --                         ------      ----
[ 1] 22                         ALLOW IN    Anywhere
[ 2] 443                        ALLOW IN    Anywhere
```

`ufw status verbose`

Provides a more detailed output, including the firewall's status, logging settings, default policies (e.g., default behavior for incoming/outgoing connections), and the rules.

Example Output:

```plaintext
Status: active
Logging: on (low)
Default: deny (incoming), allow (outgoing), disabled (routed)
New profiles: skip

To                         Action      From
--                         ------      ----
22                         ALLOW IN    Anywhere
443                        ALLOW IN    Anywhere
```
