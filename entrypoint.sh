#!/bin/sh

# 환경 변수에 따라 설정 파일 링크 설정
if [ "$ENV" = "production" ]; then
    ln -sf prod.py config/settings.py
elif [ "$ENV" = "local" ]; then
    ln -sf local.py config/settings.py
else
    echo "Warning: No valid ENV variable set. Using default (prod.py)."
    ln -sf prod.py config/settings.py
fi

# 데이터베이스 마이그레이션
python manage.py makemigrations
python manage.py migrate

# 추가적인 명령어가 있다면 여기에서 실행
# exec "$@"
