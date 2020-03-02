#!/bin/zsh
# You should add following line to your .zshrc :
# Change LEARNSCALE_SET_PATH by the path to this file
# source LEARNSCALE_SET_PATH

current_path=$0:A
PATH_TO_THE_LEARN_SCALE_MAIN_PY=current_path+/main.py

if [[ -v PERIOD ]]; then
    # set to half an hour
    PERIOD=1800
fi

if [[ -v periodic_functions ]]; then
    periodic_functions=(python3 $PATH_TO_THE_LEARN_SCALE_MAIN_PY)
else
    periodic_functions+=(python3 $PATH_TO_THE_LEARN_SCALE_MAIN_PY)
fi


