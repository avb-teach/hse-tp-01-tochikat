#!/usr/bin/env bash

INPUT=$1
OUTPUT=$2
MAX_DEPTH=0

#while [ -n "$1" ]
#do
#case "$1" in
#--max_depth) MAX_DEPTH=$2 ;;
#esac
#shift
#done

RESULT=$(python3 script.py $INPUT $OUTPUT $MAX_DEPTH 2>&1)
# echo -e $RESULT
