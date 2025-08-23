#!/bin/bash

set -e
source deployment/pre-deploy/mysql/.env

kubectl create secret generic mysql-root-password \
    --namespace pulse \
    --from-literal=password=$MYSQL_ROOT_PASSWORD

kubectl apply -k deployment/pre-deploy/mysql