#!/bin/sh

echo "Starting client ..."

if [ $DEBUG = 0 ]; then
    echo "Using production mode"
    echo "Creating production build ..."
    npm run build
    echo "Not implemented"
    exit 0
else
    echo "Using development mode"
    npm run start
fi
