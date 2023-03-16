.PHONY: build

build:
	sam build --use-container

deploy-infra:
	sam build --use-container && sam deploy

deploy-infra-guided:
	sam build --use-container && sam deploy --guided

deploy-site:
	aws s3 sync ./resume-site s3://cloudresumechallenge-website

deploy-all-from-scratch:
	sam build --use-container && sam deploy && aws s3 sync ./resume-site s3://cloudresumechallenge-website

deploy-all-from-scratch-guided:
sam build --use-container && sam deploy --guided && aws s3 sync ./resume-site s3://cloudresumechallenge-website

# Steps to create website
# 1. Build and deploy
# 2. Ensure that URLs for lambda functions are correct in index.html javascript
# 3. Sync website pages to s3 bucket with deploy-site (aws s3 sync)