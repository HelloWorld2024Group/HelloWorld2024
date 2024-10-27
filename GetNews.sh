#!/bin/bash

cd HelloWorld2024

source NewsAppEnv/bin/activate

export TOGETHER_API_KEY="API_KEY"

read sources

python GetNews.py $sources

echo "$(<summaries.json)"