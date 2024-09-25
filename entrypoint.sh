#!/bin/sh

ln -sf prod.py config/settings.py
#ln -sf local.py config/settings.py

python manage.py makemigrations
python manage.py migrate
