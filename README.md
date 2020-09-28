# aws-lambda-version-api-pipeline

###### Brian Jopling, September 2020

# Description

Contains the CloudFormation infrastructure as code for a CICD Pipeline that deploys both infra and code changes to an API. The API consists of an API Gateway whose Stages are backed by different Lambda Versions & Aliases. 

This project expects there to be 3 different accounts: a Dev, Prod, and Tools. The Tools account is where the CICD Pipeline resides in, which uses cross-account IAM roles to perform deployments in Dev & Prod.

# Usage Steps

1. In Tools Account, deploy `tooling-prereq.yaml` with CodeBuildCondition parameter set to false.
2. In Dev Account, deploy `dev-prereq.yaml`.
3. In Tools Account, deploy `toolings.yaml` with CrossAccountCondition set to false.
4. Create a change set for the stack created in step “1” (`tooling-prereq.yaml`) with the `CodeBuildCondition` parameter set to `true`.
5. Create a change set for the stack created in step “3” (`toolings.yaml`) with `CrossAccountCondition` set to `true`.
