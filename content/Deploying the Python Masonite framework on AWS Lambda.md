---
title: Deploying the Python Masonite framework on Lambda
keywords:
  - Python Masonite
  - AWS
  - Serverless
  - GitHub Actions
  - Workflow
  - API Gateway
  - Lambda
description: "Deploy the Python Masonite framework on AWS Lambda and use GitHub for deployment. Create a Lambda function, write the Lambda entry point, and configure a GitHub workflow YAML file. Set up an API Gateway and configure the custom domain for access."
created: 2025-01-27 15:28:55
updated: 2025-01-28 15:50:14
---

## Create Lambda function

[AWS Lambda Home - region us-east-1](https://us-east-1.console.aws.amazon.com/lambda/home?region=us-east-1#/functions)

- Click 'Create function'
- Input 'Function name'
- Runtime: Python 3.11

## Lambda handler

Create the `lambda_function.py` file in the root directory of the project.

[Source code](https://github.com/chris1ding1/on-serverless)

```python
from wsgi import application
import sys
import base64
from io import BytesIO
from urllib.parse import urlencode

def lambda_handler(event, context):
    headers = event.get('headers', {})

    if event['headers'].get('X-Forwarded-Proto'):
        scheme = event['headers']['X-Forwarded-Proto']
    elif event['headers'].get('CloudFront-Forwarded-Proto'):
        scheme = event['headers']['CloudFront-Forwarded-Proto']
    else:
        scheme = 'https'

    if scheme == 'http':
        port = '80'
    else:
        port = '443'

    environ = {
        'REQUEST_METHOD': event['httpMethod'],
        'PATH_INFO': event['path'],
        'QUERY_STRING': urlencode(event.get('queryStringParameters', '') or ''),
        # 'CONTENT_TYPE': '',
        # 'CONTENT_LENGTH': '',
        'SERVER_NAME': event['requestContext']['domainName'],
        'SERVER_PORT': port,
        'SERVER_PROTOCOL': event['requestContext']['protocol'],
        'wsgi.version': (1, 0),
        'wsgi.url_scheme': scheme,
        'wsgi.input': BytesIO((event.get('body') or '').encode('utf-8')),
        'wsgi.errors': sys.stderr,
        'wsgi.multithread': False,
        'wsgi.multiprocess': False,
        'wsgi.run_once': False,
    }

    for header, value in headers.items():
        header_key = 'HTTP_' + header.upper().replace('-', '_')
        environ[header_key] = value

    response_data = {'status': None, 'headers': None}

    def start_response(status, response_headers, exc_info=None):
        if exc_info:
            try:
                if response_data['status'] is not None:
                    raise exc_info[1].with_traceback(exc_info[2])
            finally:
                exc_info = None
        response_data['status'] = status
        response_data['headers'] = response_headers
        return lambda body: None

    try:
        response_iter = application(environ, start_response)
        response_body = b''.join(response_iter)
        if response_data['status'] is None:
            raise RuntimeError('start_response() was not called')

        status_code = int(response_data['status'].split(' ')[0])
        headers = dict(response_data['headers'])

        is_base64_encoded = False
        content_type = headers.get('Content-Type', 'application/octet-stream')

        is_text = (
            content_type.startswith('text/') or content_type in {
                'application/json',
                'application/xml',
                'application/javascript',
                'application/css'
            } or
            'charset' in content_type.lower() or
            content_type == 'image/svg+xml'
        )

        if not is_text and response_body:
            response_body = base64.b64encode(response_body).decode('utf-8')
            is_base64_encoded = True

        return {
            'statusCode': status_code,
            'headers': headers,
            'body': response_body,
            'isBase64Encoded': is_base64_encoded
        }
    except Exception as e:
        print(f"Error: {str(e)}")
        return {
            'statusCode': 500,
            'body': 'Internal Server Error'
        }
```

## GitHub

### Actions secrets and variables

Repositorie -> Settings -> Secrets and Variables -> Actions

- Add `AWS_ACCESS_KEY_ID` and `AWS_SECRET_ACCESS_KEY` (Secrets).
- Add `LAMBDA_FUNC_NAME` (Variables).

### Actions

Create the `.github/workflows/lambda.yml` within the project.

```yml
name: AWS Lambda Deploy

on:
  workflow_dispatch:

jobs:
  Start:
    runs-on: ubuntu-22.04
    steps:
      - name: Checkout code
        uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.11'
          cache: 'pip'

      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install -r requirements.txt --target ./

      - name: Package application
        run: |
          cp .env-example .env
          python craft key
          zip -r source-code-package.zip . -x ".git*" "__pycache__/*"

      - name: Configure AWS Credentials
        uses: aws-actions/configure-aws-credentials@v4
        with:
          aws-access-key-id: ${{ secrets.AWS_ACCESS_KEY_ID }}
          aws-secret-access-key: ${{ secrets.AWS_SECRET_ACCESS_KEY }}
          aws-region: us-east-1

      - name: To Lambda
        run: aws lambda update-function-code --function-name ${{ vars.LAMBDA_FUNC_NAME }} --zip-file fileb://source-code-package.zip

      - name: Verify deployment
        run: |
          aws lambda get-function --function-name ${{ vars.LAMBDA_FUNC_NAME }} --query 'Configuration.[LastModified, State, LastUpdateStatus]' --output table
```

## Deploy

GitHub -> Repositorie -> Actions -> AWS Lambda Deploy -> Run workflow.

Currently, deployment is triggered manually. To enable automatic deployment on push, replace `workflow_dispatch:` with the following code:

```yml
  push:
    branches:
      - main
```

## Domain

### AWS API Gateway

#### Create resource

Notes:

- {proxy+}
- Enable CORS
- Lambda proxy integration
- Setting: Binary media types (e.g. \*/\*)

#### Custom domain name

After creating a custom domain name on the AWS API Gateway, Add the domain dns record.

- type: CNAME
- value: API Gateway domain name (e.g. *.cloudfront.net)
