#!/bin/bash

set -e

# check env
if [ -z "$DJANGO_SECRET_KEY" ] || [ -z "$DB_HOST" ] || [ -z "$DB_USER" ] || [ -z "$DB_PASS" ] || [ -z "$ENVIRONMENT" ]; then
  echo "Missing required environment variables."
  exit 1
fi

# create db and initial schema
echo "Creating database if it doesn't already exist..."
mysql --execute "CREATE DATABASE IF NOT EXISTS pulse;" \
    --host "$DB_HOST" \
    --user "$DB_USER" \
    --password="$DB_PASS" \
    --ssl=false # TODO: set up certs

echo "Generating and running migrations..."
pipenv run python manage.py makemigrations
pipenv run python manage.py migrate

# run django server
# if [ "$ENVIRONMENT" = "production" ]; then
#   echo "Starting Gunicorn server..."
#   pipenv run gunicorn pulse_api.wsgi:application --bind 0.0.0.0:8000
# else
#   echo "Starting development server..."
#   pipenv run python manage.py runserver 0.0.0.0:8000
# fi

sleep infinity