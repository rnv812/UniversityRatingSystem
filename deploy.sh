#!/bin/bash
if [[ $1 = "prod" || $1 = "dev" ]]; then
    fileEnv="docker-compose.${1}.yaml"
    flags=${@:2}
    echo "Running docker compose -f $fileEnv up $flags"
    docker compose -f $fileEnv up $flags
else
    echo "Use following format ./deploy.sh prod|dev [options]"
    echo
    echo "Possible options at https://docs.docker.com/engine/reference/commandline/compose_up/#options"
fi