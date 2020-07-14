#!/bin/bash
set -ex
python3 manage.py migrate
python3 manage.py loaddata library/fixtures/fixtures.json