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

echo "Applying database migrations..."
python manage.py migrate
echo "You can use load-fixture.sh script to prepopulate database with some values"

echo "Creating admin user..."
python manage.py createsuperuser --email $DJANGO_SUPERUSER_EMAIL --no-input

echo "Running server on port $DJANGO_SERVER_PORT ..."

if [ $DEBUG = 0 ]; then
  echo "Using production mode"
  echo "Performing security checks..."
  python manage.py check --deploy
  echo "Not implemented"
  exit 0
else
  echo "Using development mode"
  python manage.py runserver 0.0.0.0:$DJANGO_SERVER_PORT
fi

echo "Server has started"

exec "$@"