# pulse-api
API backend for Pulse: Social Media for Humans

## Deployment with Jenkins
This project currently deploys to my self-hosted kubernetes cluster using pre-defined kubernetes resources found in the `deployment/` directory.  The `deployment/pre-deploy/pre-deploy.sh` script declares the namespace and serviceaccount used by jenkins to deploy the rest of the app after building.  It must be run once before building.

The mysql server is currently not managed with Jenkins, it can be deployed with the install script in `deployment/pre-deploy/mysql/install.sh`

## Local Setup
`docker compose up -d --build`