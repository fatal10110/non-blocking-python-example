#!/bin/bash
DIR="$( cd "$(dirname "$0")" ; pwd -P )"

tmux new-session -s $1 "sh $DIR/$1.sh $DIR; read"
