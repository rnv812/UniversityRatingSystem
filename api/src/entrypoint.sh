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
echo "You can use localize.sh script to switch to presented locale"

echo "Creating superuser..."
python manage.py shell < create_superuser.py

if [ $? = 0 ]; then
    echo "Superuser '$DJANGO_SUPERUSER_EMAIL' created successfully"
else
    echo "Superuser '$DJANGO_SUPERUSER_EMAIL' is already exists"
fi

echo "Running server ..."

if [ "$DEPLOY_ENV" = "prod" ]; then
    echo "Using production mode"
    echo "Performing security checks..."
    python manage.py check --deploy
    echo "Not implemented"
    exit 0
else
    echo "Using development mode"
    python manage.py runserver 0.0.0.0:8000
fi
