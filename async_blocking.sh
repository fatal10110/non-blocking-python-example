#!/bin/bash
tmux split-window -h "docker run -v $1/src/examples:/example --rm -ti --network="host" example python async-blocking/server.py"
sleep 2
tmux split-window -h "docker run -v $1/src/examples:/example --rm -ti --network="host" example python async-blocking/client.py; read"
tmux select-layout even-horizontal
docker run -v $1/src/examples:/example --rm -ti --network="host" example python async-blocking/client_async.py
