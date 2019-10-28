#!/bin/bash

tmux split-window -h "docker run -v $1/src/examples:/example --rm -ti --network="host" example python async-context/context_var.py; read"
docker run -v $1/src/examples:/example --rm -ti --network="host" example python async-context/thread_local.py
