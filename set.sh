#!/bin/zsh
# You should add following lines to your .zshrc
### LEARN SCALE ### START ###

if [[ -v PERIOD ]]; then
    # set to half an hour
    PERIOD=1800
fi

if [[ -v periodic_functions ]]; then
    periodic_functions=($PATH_TO_THE_LEARN_SCALE_MAIN_PY)
else
    periodic_functions+=($PATH_TO_THE_LEARN_SCALE_MAIN_PY)
fi

### LEARN SCALE ### END ###

