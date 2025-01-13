#!/bin/bash

export PYTHON_VERSION=3.13

python3 -m pip install --upgrade pip
python3 -m pip install -r requirements.txt
python3 generate.py
