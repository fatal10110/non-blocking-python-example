#!/bin/bash

tmux split-window -h "docker run -v $1/src/examples:/example --rm -ti --network="host" example python async-non-blocking/server.py"
tmux split-window -h "docker run -v $1/src/examples:/example --rm -ti --network="host" example python async-non-blocking/server.py 5678 read"
tmux select-layout even-horizontal
sleep 1
docker run -v $1/src/examples:/example --rm -ti --network="host" example python async-non-blocking/client.py
