#!/bin/sh

test_value="100 200 300"

for value in $test_value; do
    for f in q1v*.py; do
        if [ -f "$f" ]; then
            echo "--> Test file $f with value $value :";
            python3.4 $f $value
        fi
    done
done