#!/bin/sh
# run Object Calisthenics rules against lcd
export PYTHONPATH=pylint:$PYTHONPATH
pylint --rcfile ./objectcalisthenics.pylintrc lcd
