#!/bin/bash

set -e
source jenkins/.env

# Create namespace and service account for jenkins to use
kubectl apply -f ./jenkins/pre-deploy/namespace.yaml 
kubectl apply -f ./jenkins/pre-deploy/serviceaccount.yaml

# Harbor registry URL and secret
kubectl delete secret harbor-registry-secret --namespace pulse || true
kubectl create secret docker-registry harbor-registry-secret \
  --docker-server=${HARBOR_SERVER} \
  --docker-username=${HARBOR_USERNAME} \
  --docker-password=${HARBOR_PASSWORD} \
  --docker-email=${HARBOR_EMAIL} \
  --namespace pulse