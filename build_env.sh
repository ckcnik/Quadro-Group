#!/bin/bash
echo $0: Creating virtual environment
virtualenv --prompt="<store>" ./env

mkdir ./logs
touch ./logs/gunicorn_supervisor.log
mkdir ./locale # для интернационализации

source ./env/bin/activate
export PIP_REQUIRE_VIRTUALENV=true
echo $0: Installing dependencies
./env/bin/pip3.4 install --requirement=./requirements/$1.txt --log=./logs/build_pip_packages.log
echo $0: Collectstatic
./env/bin/python3.4 manage.py collectstatic # статика

echo $0: Making virtual environment relocatable
virtualenv --relocatable ./env

echo $0: Creating virtual environment finished.