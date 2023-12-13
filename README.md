**Overview**

[The Cloud Resume Challenge](https://cloudresumechallenge.dev/docs/the-challenge/aws/) is a hands-on project designed to help you bridge the gap from cloud certification to cloud job. It incorporates many of the skills that real cloud and DevOps engineers use in their daily work.

https://jackgoggin.com - a secure, scalable, serverless web application on AWS with automated deployment pipelines.

**Benefits of the challenge
**

As a pure software developer, this challenge taught me the more DevOps and Cloud related skills to become a more well rounded engineer, make better design decisions for more scalable applications as well as the ability to implement that design in an E2E fashion rather than just being a 'coder', I can now build the whole pipeline.

Software Development (Frontend / Backend perspective)
IaC (Infrastructure as Code) using SAM
CI/CD (GitHub actions)
Serverless Architecture on AWS (Lambda, API Gateway, DynamoDB, S3)
Security (IAM, bucket policies, API authentication/authorization)
Networking (DNS if using Route53)
many more!

**What was used?**

## Frontend Development
- HTML
- CSS
- JavaScript

## Backend Development
- Python - to update the visitor counter within lambda, and write unit tests

## Cloud Infrastructure (AWS)
- Amazon Web Services (AWS):
  - S3 (Simple Storage Service) - store my static files (HTML/CSS/JS)
  - CloudFront (Content Delivery Network) - delivery my content
  - Route 53 - for domain registration https://jackgoggin.com
  - Certificate Manager - secure the website with HTTPS
  - DynamoDB - store the visitor counter with NOSQL
  - API Gateway - handle HTTP requests and point them to our lambda services
  - Lambda - serverless computing and housed my python functions
  - Identity and Access Management (IAM) - give access to AWS resources, such as my SAM model to define and deploy services
  - Serverless Application Model (SAM) - Infrastructure as Code service to autoatically deploy my E2E application

## Continuous Integration and Deployment (CI/CD)
- GitHub Actions - automate the build, test and deployment of my application

**How do these work together?**

For more information check out my blog on the development of this application - https://dev.to/jackhenryg/my-cloud-resume-challenge-4e6i.

