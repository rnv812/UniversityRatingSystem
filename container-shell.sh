#!/bin/bash
# connect terminal to container with specified user  
if [ $# = 2 ]; then
    containerId=$(docker ps -aqf "name=$1")
    if [ $containerId ]; then
        docker exec -u $2 -it $containerId /bin/sh
    else
        echo "No running container with name $1"
    fi
else
    echo "Use following format: container-shell.sh <container name> <user>"
    echo
    echo "Example usage: container-shell.sh urs-api-dev root"
fi
