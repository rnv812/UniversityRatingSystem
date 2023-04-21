#!/bin/bash
# connect terminal to container with specified user  
if [ $# = 2 ]; then
    containerId=$(docker ps -aqf "name=$1")
    if [ $containerId ]; then
        echo $containerId
        docker exec -u $2 -it $containerId /bin/sh
    else
        echo "No running container with name $1"
    fi
else
    echo "Use following format: service-shell.sh <container> <user>"
    echo
    echo "Example usage: service-shell.sh dev api root"
fi
