#!/bin/bash

set -e
source kubernetes/.env

if [[ -z "${HARBOR_SERVER}" || -z "${HARBOR_USERNAME}" || -z "${HARBOR_PASSWORD}" || -z "${HARBOR_EMAIL}" ]]; then
  echo "Error: One or more environment variables are not set."
  exit 1
fi

# Create namespace and service account for jenkins to use
kubectl apply -f ./kubernetes/namespace.yaml 
kubectl apply -f ./kubernetes/serviceaccount.yaml

# Harbor registry URL and secret
kubectl delete secret harbor-registry-secret --namespace pulse || true
kubectl create secret docker-registry harbor-registry-secret \
  --docker-server=${HARBOR_SERVER} \
  --docker-username=${HARBOR_USERNAME} \
  --docker-password=${HARBOR_PASSWORD} \
  --docker-email=${HARBOR_EMAIL} \
  --namespace pulse

# add harbor to talos cluster
source kubernetes/.env
envsubst < ./kubernetes/registry_patch.template.yaml > /tmp/registry_patch.yaml
talosctlwrapper all patch machineconfig --patch @/tmp/registry_patch.yaml