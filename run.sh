#!/bin/bash

SCRIPT_DIR=$( cd "$(dirname "${BASH_SOURCE[0]}")" ; pwd -P )
DOS_PATH=$(echo $SCRIPT_DIR | sed 's/^\/\{1,2\}mnt\/\(.\)/\1:/')


tmux new-session -s $1 "sh $SCRIPT_DIR/$1.sh $DOS_PATH; read"
