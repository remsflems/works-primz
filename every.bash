#!/bin/bash

python algo.py prime.txt.bkp cd b5

for entry in "cdb5"/*
do
  python algo.py "$entry" 57 a4
done

for entry in "57a4"/*
do
  python algo.py "$entry" 54 16
done

for entry in "5416"/*
do
  python algo.py "$entry" 12 f4
done

for entry in "12f4"/*
do
  python algo.py "$entry" fb 7f
done





