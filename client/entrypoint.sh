#!/bin/sh

echo "Starting client ..."

if [ $DEPLOY_ENV = "prod" ]; then
    echo "Using production mode"
    echo "Creating production build ..."
    npm run build
    echo "Not implemented"
    exit 0
else
    echo "Using development mode"
    npm run start
fi
