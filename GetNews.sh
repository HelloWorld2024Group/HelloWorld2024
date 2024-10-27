#!/bin/bash

cd HelloWorld2024

source NewsAppEnv/bin/activate

read sources

python GetNews.py $sources

echo "$(<[json file])"