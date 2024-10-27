#!/bin/bash

cd HelloWorld2024

source NewsAppEnv/bin/activate

python ArticleDatabaseCreator.py

python Summarizer.py