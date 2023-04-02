#!/bin/bash
# connect terminal to web container shell with specified user  
if [[ $1 = "dev" || $1 = "prod" ]]; then
    containerId=$(docker ps -aqf "name=urs-web-$1")
    if [ $containerId ]; then
        docker exec -u $2 -it $containerId /bin/sh
    else
        echo "No running container with name urs-web-$1"
    fi
else
    echo "Use following format: shell-web.sh dev|prod <user>"
fi