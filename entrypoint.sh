#!/bin/bash

cd /opt/class_project
python ./manage.py migrate
python ./manage.py runserver 0.0.0.0:8000
