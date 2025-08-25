# pulse-api

![Django](https://img.shields.io/badge/Django-5.2.5-green)
![Django REST Framework](https://img.shields.io/badge/DRF-3.16.1-red)
![MySQL](https://img.shields.io/badge/MySQL-2.2.7-blue)
![Gunicorn](https://img.shields.io/badge/Gunicorn-23.0.0-brightgreen)
![Boto3](https://img.shields.io/badge/Boto3-1.40.13-yellow)
![Pillow](https://img.shields.io/badge/Pillow-11.3.0-orange)

API backend for Pulse: Social Media for Humans

## Deployment with Jenkins
This project currently deploys to my self-hosted kubernetes cluster using pre-defined kubernetes resources found in the `deployment/` directory.  The `deployment/pre-deploy/pre-deploy.sh` script declares the namespace and serviceaccount used by jenkins to deploy the rest of the app after building.  It must be run once before building.

The mysql server is currently not managed with Jenkins, it can be deployed with the install script in `deployment/pre-deploy/mysql/install.sh`

## Local Setup
`docker compose up -d --build`