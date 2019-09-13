#!/usr/bin/env bash

echo "\n------\n Building the Image\n---------\n\n"

docker-compose -f docker-compose.common.yml -f docker-compose.dev.yml build

echo "\n------\n Pulling up the contains.\n---------\n\n"


docker-compose -f docker-compose.common.yml -f docker-compose.dev.yml up -d
