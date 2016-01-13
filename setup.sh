#!/bin/bash
set -eux
cd $(pwd)
virtualenv env
./env/bin/pip install --upgrade pip
./env/bin/pip install -r requirements.txt
./env/bin/python setup.py develop
