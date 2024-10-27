#!/bin/bash

cd HelloWorld2024

source NewsAppEnv/bin/activate

export TOGETHER_API_KEY="API_KEY"

python Fetcher.py

touch log.txt

timestamp=$(date +"%Y-%m-%d %H:%M:%S")

echo "Database updated at $timestamp" >> log.txt