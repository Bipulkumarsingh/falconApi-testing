#!/bin/bash

set -e 

python3 -m pytest -vv --html=report.html --self-contained-html
