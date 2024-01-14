
# About

This repo was built to setup email notifications of significant changes in stocks and funds. A simple strategy using the weekly RSI and MFI to indicate whether oversold (RSI & MFI < 50) or overbought (RSI & MFI > 70).

A cron job is setup on an AWS EC2 instance to run a Docker container every Monday morning. The script loops over markets in a list and sends an email via AWS SES to notify of buying and selling opportunities.

# Built With
Frameworks:
- Python
- Docker
- AWS (SES, ECR, EC2)

Libraries:
- Yahoo Finance
- Pandas
- Simple Mail Transfer Protocol (SMTP)



# Usage

Clone repository
```powershell
git clone https://github.com/AndyW1990/rsi-mfi-notify.git
```
## Using and editing the package locally
Navigate to the project directory and EITHER:

OPTION 1: Setup environment. You will need to update the .env with your AWS credentials after.
```powershell
make setup_env
```

OPTION 2: Basic setup. You will need to change app/params.py with your AWS credentials, as opposed to calling environment variables (Local only, do not share).
```powershell
pip install -e . 
```

## Setting up the Docker container

Rename the sample Dockerfile then update with your SES credentials.
```powershell
mv Dockerfile_sample Dockerfile
```

Build the docker image locally (Change env vars if not using them). If you wish to test functionality, first modify the function call in app/main.py with appropriate test values as keyword arguments.
```powershell
docker build --tag=$IMAGE_NAME:$TAG .
```


Create a repository in AWS ECR and follow the push commands. If using  env vars you can use the Makefile.
```powershell
make docker_push
```

Pull the image to your EC2 instance. Commands for AWS (changing the env vars unless setup in your instance).
```powershell
docker pull $AWS_ID.dkr.ecr.$AWS_REGION.amazonaws.com/$IMAGE_NAME:$TAG
```

Add to crontab to setup the execution of container (again changing env vars).
```powershell
#write out current crontab
crontab -l > mycron
#echo new cron into cron file
echo "00 08 * * 1 docker run --rm $AWS_ID.dkr.ecr.$AWS_REGION.amazonaws.com/$IMAGE_NAME:$TAG" >> mycron
#install new cron file
crontab mycron
rm mycron
```