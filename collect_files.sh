#!/usr/bin/env bash

INPUT=$1
OUTPUT=$2

RESULT=$(python3 script.py $INPUT $OUTPUT 2>&1)
# echo -e $RESULT
