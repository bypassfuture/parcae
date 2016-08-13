#!/bin/bash

ENVDIR=$PWD/../../ENV
export PYTHONPATH="$ENVDIR:$PWD:$PWD/../lib:$PYTHONPATH"
export PATH="$ENVDIR/bin:$PATH"
