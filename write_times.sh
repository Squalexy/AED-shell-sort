#!/bin/sh
for python_file_name in $(find ./inputs/ -name *.txt)
do
   pypy3 ./shell_sort.py < $python_file_name
done