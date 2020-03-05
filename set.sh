#!/bin/zsh
# You should add following line to your .zshrc :
# Change LEARNSCALE_SET_PATH by the path to this file
# source LEARNSCALE_SET_PATH

PATH_TO_THE_LEARN_SCALE_MAIN_PY=${0%/*}/main.py

if [[ ! -v PERIOD ]]; then
    # set to half an hour
    export PERIOD=1800
fi


__call_learn_scale () { python3 $PATH_TO_THE_LEARN_SCALE_MAIN_PY }
periodic_functions+=(__call_learn_scale)


