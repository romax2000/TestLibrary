#!/bin/bash
set -ex
celery -A library worker --pool=solo -l info