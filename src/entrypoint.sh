#!/bin/sh

echo "Waiting for database..."

while ! nc -z $DB_HOST $DB_PORT; do
  sleep 1
done

echo "Activation environment..."

if [ -d "../.venv/" ]; then
  source ../.venv/bin/activate
else
  echo "No .venv/ found in the /app directory"
  exit 1
fi

echo "Running server..."

if [ $DEBUG = 0 ]; then
  echo "Using production mode"
  echo "Not implemented"
  exit 0
else
  echo "Using development mode"
  python manage.py runserver 8000
fi

echo "Server has started"

exec "$@"