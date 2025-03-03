---
title: "GitHub Actions Guide"
keywords:
  - GitHub
  - CI/CD
  - Python
  - Node
  - YAML
  - Auth
  - AWS
  - Workflow syntax
  - Git
  - Checkout
  - Setup
description: "A practical guide to GitHub Actions workflow syntax and common configurations for setting up effective CI/CD pipelines."
created: 2025-03-03 05:27:18
updated: 2025-03-03 05:27:18
---

[GitHub Actions documentation](https://docs.github.com/en/actions)

Workflow files use YAML syntax, and must have either a .yml or .yaml file extension. You must store workflow files in the `.github/workflows` directory of your repository.

## On

You can define single or multiple events that can trigger a workflow, or set a time schedule. You can also restrict the execution of a workflow to only occur for specific files, tags, or branch changes.

[On - GitHub Actions Docs](https://docs.github.com/en/actions/writing-workflows/workflow-syntax-for-github-actions#on)

Runs on any push to any branch.

```yml
on: push
```

```yml
on: [push]
```

You can specify a single event or multiple events. For example, a workflow with the following on value will run when a push is made to any branch in the repository or when someone forks the repository:

```yml
on: [push, fork]
```

Runs only on pushes to `main` branch.

```yml
on:
  push:
    branches:
      - main
      [- branche name]
```

Runs only when manually triggered.

```yml
on:
  workflow_dispatch:
```

Runs on pushes to main branch OR when manually triggered.

```yml
on:
  push:
    branches:
      - main
  workflow_dispatch:
```

## Checkout

[Checks-out your repository](https://github.com/actions/checkout)

```yml
- name: Checkout code
  uses: actions/checkout@v4
```

## Setup Development Environments

[Setup Python](https://github.com/actions/setup-python)

```yml
- name: Set Python
    uses: actions/setup-python@v5
      with:
        python-version: '3.11'
        cache: 'pip'
```

[Setup Node](https://github.com/actions/setup-node)

```yml
- name: Set Node
  uses: actions/setup-node@v4
    with:
      node-version: 20
      cache: 'npm'
```

## Configure Authentication Credentials

### AWS

[AWS Credentials](https://github.com/aws-actions/configure-aws-credentials)

```yml
- name: Configure AWS Credentials
  uses: aws-actions/configure-aws-credentials@v4
  with:
    aws-access-key-id: ${{ secrets.AWS_ACCESS_KEY_ID }}
    aws-secret-access-key: ${{ secrets.AWS_SECRET_ACCESS_KEY }}
    aws-region: us-east-1
```

## Examples

[Jobs - GitHub Actions Docs](https://docs.github.com/en/actions/writing-workflows/workflow-syntax-for-github-actions#jobs)

Use `jobs.<job_id>` to give your job a unique identifier. The key job_id is a string and its value is a map of the job's configuration data. You must replace `<job_id>` with a string that is unique to the jobs object. The `<job_id>` must start with a letter or _ and contain only alphanumeric characters, -, or _.

Use `jobs.<job_id>.needs` to identify any jobs that must complete successfully before this job will run.

Use `jobs.<job_id>.runs-on` to define the type of machine to run the job on. [runs-on - GitHub Actions Docs](https://docs.github.com/en/actions/writing-workflows/workflow-syntax-for-github-actions#jobsjob_idruns-on)

`jobs.<job_id>.steps[*].run`: Each run keyword represents a new process and shell in the runner environment. When you provide multi-line commands, each line runs in the same shell.

```yml
name: <The name of the workflow>
on:
  push:
    branches:
      - main
  workflow_dispatch:
jobs:
  <job id 1>:
    runs-on: ubuntu-22.04
    steps:
      - name: Checkout code
        uses: actions/checkout@v4
      - name: <step name>
        run: <command. e.g. `echo Hello World`>
      - name: <step name>
        run: |
          <command. e.g. `echo Hello`>
          <command. e.g. `echo World`>
  [job id 2:]
    [needs: <job id 1>]
  [job id 3:]
    [needs: <job id 1, job id 2>]
```
