#!/bin/sh


# 데이터베이스 마이그레이션
python manage.py makemigrations
python manage.py migrate

# 추가적인 명령어가 있다면 여기에서 실행
python manage.py runserver 0.0.0.0:8000
