# Python 3.12 이미지를 베이스 이미지로 사용
FROM python:3.12

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
# 이미지에 대한 메타정보를 추가
LABEL authors="Fillsogood"

# pip을 최신 버전으로 업그레이드하고, poetry 패키지를 설치
RUN pip install --upgrade pip \            
    && pip install poetry                  

# 컨테이너 내 작업 디렉터리를 /backend로 설정
WORKDIR /backend

# 프로젝트의 pyproject.toml 파일과 poetry.lock 파일을 컨테이너로 복사
COPY ./pyproject.toml ./poetry.lock* ./

# poetry 설정 및 의존성 설치
RUN poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-ansi || echo "No logs available."

# 나머지 파일 복사
COPY ./manage.py ./manage.py
COPY ./config ./config
COPY ./apps ./apps
COPY ./entrypoint.sh ./entrypoint.sh

# entrypoint.sh에 실행 권한 부여
RUN chmod +x ./entrypoint.sh

# 컨테이너 시작 시 entrypoint.sh 스크립트를 실행하도록 설정
ENTRYPOINT ["./entrypoint.sh"]
