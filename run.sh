#!/bin/bash

source /home/ubuntu/Bitbucket/collector/bin/activate

exec uwsgi --ini /home/ubuntu/Bitbucket/collector/env/uwsgi.ini --py-autoreload 1
