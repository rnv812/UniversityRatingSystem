#!/bin/bash
if [[ $1 = "prod" || $1 = "dev"] && [$2 = "down" || $2 = "up" ]]; then
    cd ..
    fileEnv="docker-compose.${1}.yaml"
    action=$2
    flags=${@:2}
    echo "Running docker compose -f $fileEnv $action $flags"
    docker compose -f $fileEnv $action $flags
else
    echo "Use following format ./deploy.sh prod|dev down|up [compose opts]"
fi