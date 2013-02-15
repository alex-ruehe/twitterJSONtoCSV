#!/bin/bash

directory=$1

for file in $( ls $directory )
do
	if [ ${file: -3} == ".js" ]; then
    	python extract.py $directory$file
	fi
done