#!/bin/bash
if [[ $1 = "prod"  || $1 = "dev"]] && [[ $2 = "down" || $2 = "up" ]]; then
    cd ..
    fileEnv="docker-compose.${1}.yml"
    action=$2
    echo "Running docker compose -f docker-compose.yaml -f $fileEnv $action"
    docker compose -f docker-compose.yaml -f $fileEnv $action
else
    echo "Use following format ./deploy.sh prod|dev down|up"
fi