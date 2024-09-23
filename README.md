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