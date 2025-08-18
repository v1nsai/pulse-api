#!/bin/bash

set -e

# create db and initial schema
mysql --execute "CREATE DATABASE IF NOT EXISTS $DB_NAME;" \
    --host "$DB_HOST" \
    --user "$DB_USER" \
    --password="$DB_PASS" \
    --ssl=false
pipenv run python manage.py migrate

# run django server
pipenv run python manage.py runserver 0.0.0.0:8000
