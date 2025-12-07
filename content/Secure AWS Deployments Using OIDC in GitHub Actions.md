---
title: "Secure AWS Deployments Using OIDC in GitHub Actions"
slug: 'secure-aws-deployments-using-oidc-in-github-actions'
keywords:
  - OIDC
  - GitHub Actions
  - OpenID Connect
  - AWS
  - CI/CD
  - IAM Role
  - Assume Role
  - Keyless Authentication
  - Security
description: "Learn how to securely deploy to AWS from GitHub Actions using OIDC, eliminating the need for long-lived credentials."
created: 2025-12-07 13:01:55
updated: 2025-12-07 13:01:55
---

## Adding the identity provider to AWS

Open [AWS IAM](https://console.aws.amazon.com/iam/home) console, Select [Identity providers](https://console.aws.amazon.com/iam/home#/identity_providers), Click "Add provider":

- For the "Provider type": Select "OpenID Connect"
- For the "Provider URL": Use `https://token.actions.githubusercontent.com`
- For the "Audience": Use `sts.amazonaws.com`

## Configuring the role and trust policy on AWS

Open [AWS IAM](https://console.aws.amazon.com/iam/home) console, Select [Roles](https://console.aws.amazon.com/iam/home#/identity_providers), Click "Create role":

### Create

**Step 1: Select trusted entity**

- For the "Trusted entity type": Select "Web identity"
- For the "Identity provider": Select "token.actions.githubusercontent.com"
- For the "Audience": Select "sts.amazonaws.com"
- For the "GitHub organization": GitHub organization name
- For the "GitHub repository - optional": GitHub repository name
- For the "GitHub branch - optional": GitHub branch name

Click "Next"

**Step 2: Add permissions**

Don't select any "Permissions policies"

Click "Next"

**Step 3: Name, review, and create**

- Role name: Enter a meaningful name to identify this role.
- Description - optional: Add a short explanation for this role.

Click "Create role"

### Trust Policy Example

```json
{
	"Version": "2012-10-17",
	"Statement": [
		{
			"Effect": "Allow",
			"Principal": {
				"Federated": "arn:aws:iam::<AWS ACCOUNT ID>:oidc-provider/token.actions.githubusercontent.com"
			},
			"Action": "sts:AssumeRoleWithWebIdentity",
			"Condition": {
				"StringEquals": {
					"token.actions.githubusercontent.com:aud": "sts.amazonaws.com"
				},
				"StringLike": {
					"token.actions.githubusercontent.com:sub": [
						"repo:<GitHub org>/*", // Grants access to all repos in the org
						"repo:<GitHub org>/<GitHub repo>:*", // Grants access to any branch within the repository
						"repo:<GitHub org>/<GitHub repo>:ref:refs/heads/<GitHub branch>" // Grants access to a specific branch only
					]
				}
			}
		}
	]
}
```

## Attaching permissions to the IAM role (AWS)

- [IAM JSON policy elements: Action](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_action.html)
- [IAM JSON policy elements: Resource](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_resource.html)

```json
{
	"Version": "2012-10-17",
	"Statement": [
		{
			"Sid": "Statement1",
			"Effect": "Allow",
			"Action": [
				// <service>:<action>
			],
			"Resource": [
				// arn:aws:<service>:<region>:<account-id>:...
			]
		}
	]
}
```

Grants permission to update the specified Lambda function's code:

```json
"Action": [
	"lambda:UpdateFunctionCode"
],
"Resource": [
	"arn:aws:lambda:<region>:<account-id>:function:<function-name>"
]
```

## GitHub Actions workflow

Use the [aws-actions/configure-aws-credentials](https://github.com/aws-actions/configure-aws-credentials) action to exchange the OIDC token (JWT) for a cloud access token.

The `aws-actions/configure-aws-credentials` action receives a JWT from the GitHub OIDC provider, and then requests an access token from AWS.

```yaml
- name: Configure AWS Credentials
  uses: aws-actions/configure-aws-credentials@v<Version>
  with:
    role-to-assume: arn:aws:iam::<AWS account id>:role/<AWS IAM role name>
    aws-region: <AWS region>
```

## Also

- [GitHub - Configuring OpenID Connect in Amazon Web Services](https://docs.github.com/en/actions/how-tos/secure-your-work/security-harden-deployments/oidc-in-aws)
- [AWS - Create an OpenID Connect (OIDC) identity provider in IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_providers_create_oidc.html)
- [AWS - Configuring a role for GitHub OIDC identity provider](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create_for-idp_oidc.html#idp_oidc_Create_GitHub)