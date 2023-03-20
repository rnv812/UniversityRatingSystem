#!/bin/bash
# connect terminal to web container shell with specified user  
if [[ $1 = "root" || $1 = "app" ]]; then
    containerId=$(docker ps -aqf "name=web-dev")
    docker exec -u $1 -it $containerId /bin/sh
else
    echo "Use following format ./shell-web.sh root|app"
fi