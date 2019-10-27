#!/bin/bash

tmux split-window -h "python3 $1/src/examples/server.py"
tmux split-window -h "python3 $1/src/examples/server.py 5678 read"
tmux select-layout even-horizontal
PYTHONPATH=$1/src/examples/ python3 $1/src/examples/async-non-blocking/client.py
