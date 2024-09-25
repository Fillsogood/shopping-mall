# portfoilo-site
- 쇼핑몰

## 1일차

### poetry
- poetry init
- poetry shell
- poetry install
    > 이건 나중에 새로 받을 때 쓰는 명령어 

### 패키지 다운
- poetry add Django
- poetry add django-admin startproject config .
- poetry black >>> 코드 자동 포매터
    >pyproject.toml 에서 line-length = 120 설정
- poetry isort >>> 임포트 정렬 도구
    >pyproject.toml 에서 profile = "black" 설정
- poetry mypy >>> 정적 타입 검사 고구

### 코드 정렬 및 임포트 정렬 도구 정적 타입 검사 한 번에 치는 명령어 실행
- checks.bat 만든 후 작성
    >@echo off
    >poetry run black .
    >poetry run isort .
    >poetry run mypy .
- .\checks.bat 실행


### CI/CD 설정
- github\workflow\checks.yml에 CI 작성

## 2일차

### 모델 정의
- products
- orders
- orderitems
- common
- users
- payment
- address

### 도커 설정
- 도커 허브 들어가서 Access Token 발급
- Github 프로젝트에 secret variable 등록
    >DOCKERHUB_USER
    >DOCKERHUB_TOKEN
- Dockerfile 생성
- .dockerignore 생성
- 구조 변경

## 3일차

### 심볼 설정

-window: cmd 관리자 권한으로 설정후 mklink settings.py local.py 로컬에서 실행

- mklink settings.py prod.py 서버에서 실행

-Mac: ln -sf local.py settings.py 로컬 , ln -sf prod.py settings.py 서버

### Dockerfile 및 yml 및 entrypoint.sh 코드 생성
- nginx.conf 설정
- be     | exec ./entrypoint.sh: no such file or directory 오류 수정 중