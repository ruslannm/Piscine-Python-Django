#!/bin/sh

echo `pip3 --version | cut -d ' ' -f 2`
python3 -m venv local_lib
source local_lib/bin/activate
pip3 install -r requirements.txt
