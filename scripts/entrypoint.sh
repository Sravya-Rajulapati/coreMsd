#!/usr/bin/env bash

set -e

RUN_MANAGE_PY='poetry run python -m msd.manage'

echo 'Collecting static files...'
$RUN_MANAGE_PY collectstatic --no-input

echo 'Running migrations...'
$RUN_MANAGE_PY migrate --no-input

# Using Gunicorn with a WSGI application
exec poetry run gunicorn msd.project.wsgi:application -w 2 -b 0.0.0.0:8000
