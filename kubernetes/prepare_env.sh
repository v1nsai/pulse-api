#!/bin/bash

set -e
source kubernetes/.env

if [[ -z "${HARBOR_SERVER}" || -z "${HARBOR_USERNAME}" || -z "${HARBOR_PASSWORD}" || -z "${HARBOR_EMAIL}" ]]; then
  echo "Error: One or more environment variables are not set."
  exit 1
fi

kubectl apply -f ./kubernetes/namespace.yaml 
kubectl apply -f ./kubernetes/serviceaccount.yaml
kubectl create secret docker-registry harbor-registry-secret \
  --docker-server=${HARBOR_SERVER} \
  --docker-username=${HARBOR_USERNAME} \
  --docker-password=${HARBOR_PASSWORD} \
  --docker-email=${HARBOR_EMAIL} \
  --namespace pulse