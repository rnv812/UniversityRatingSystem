#!/bin/bash
# connect terminal to api container shell with specified user  
if [[ $1 = "dev" || $1 = "prod" ]]; then
    containerId=$(docker ps -aqf "name=urs-api-$1")
    if [ $containerId ]; then
        docker exec -u $2 -it $containerId /bin/sh
    else
        echo "No running container with name urs-api-$1"
    fi
else
    echo "Use following format: shell-api.sh dev|prod <user>"
fi