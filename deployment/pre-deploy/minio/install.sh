#!/bin/bash

set -e
source deployment/pre-deploy/minio/.env

if [ -z "$MINIO_ROOT_USER" ] || [ -z "$MINIO_ROOT_PASSWORD" ] || [ -z "$PULSE_USER" ] || [ -z "$PULSE_PASS" ]; then
  echo "Missing required environment variables."
  exit 1
fi

mc alias set myminio http://localhost:9000 $MINIO_ROOT_USER $MINIO_ROOT_PASSWORD
mc admin user add myminio $PULSE_USER $PULSE_PASS
mc admin policy create myminio pulse-bucket-policy bucket_policy.json
mc admin policy attach myminio pulse-bucket-policy --user $PULSE_USER