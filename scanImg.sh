#!/bin/bash
for i in {0..877}
do
    ((start = i))
    ((end = i + 1))
   #echo "Python3 app called with $start and $end"
   python3 createDB.py $start $end
done
