#!/bin/sh
# run Object Calisthenics rules against lcd
export PYTHONPATH=pylint/checkers:$PYTHONPATH
pylint --rcfile ./objectcalisthenics.pylintrc lcd
