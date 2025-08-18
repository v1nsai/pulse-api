#!/bin/bash

set -e
source jenkins/mysql/.env

kubectl create secret generic mysql-root-password \
    --namespace pulse \
    --from-literal=password=$MYSQL_ROOT_PASSWORD

kubectl apply -k jenkins/mysql