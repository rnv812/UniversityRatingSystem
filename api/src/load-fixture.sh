#!/bin/sh

if [ $1 ]; then
    source activate.sh &&
    gdown $1 -O fixture.json &&
    python manage.py loaddata fixture.json
else
    echo "Get fixture file from google drive and load it to database."
    echo
    echo "Use following format: ./load-fixture.sh <fixture file id>"
fi