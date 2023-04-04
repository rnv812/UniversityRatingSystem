#!/bin/sh

if [ $1 ]; then
    gdown $1 -O fixtures.zip && unzip fixtures.zip
else
    echo "Get zip file from google drive and unpack it."
    echo
    echo "Use following format: ./gdown-unzip.sh <file id>"
fi