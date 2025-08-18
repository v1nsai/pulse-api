# pulse-api
API backend for Pulse: Social Media for Humans

## Set up
This project currently deploys to my self-hosted kubernetes cluster using pre-defined kubernetes resources found in the `jenkins/` directory.  The `jenkins/pre-deploy/pre-deploy.sh` script declares the namespace and serviceaccount used by jenkins to deploy the rest of the app after building.  It must be run once before building.