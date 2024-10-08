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

### 심볼 설정 // 이제 안 씀

-window: cmd 관리자 권한으로 설정후 mklink settings.py local.py 로컬에서 실행

- mklink settings.py prod.py 서버에서 실행

-Mac: ln -sf local.py settings.py 로컬 , ln -sf prod.py settings.py 서버

### Dockerfile 및 yml 및 entrypoint.sh 코드 생성
- nginx.conf 설정
- be     | exec ./entrypoint.sh: no such file or directory 오류 수정 중

## 4일차

- DB 이미지 설정

- .entrypoint.sh 권한 오류 설정

## 5일차

- 도커 권한 오류 수정 완료
    -이슈
        > 심볼 링크를 만들어서 config에서 권한오류로 인한 문제 따라서 심볼 링크를 안 만들고 settings.py로 바꿈
        > DB 이미지 설정에서 미리 올라간 migrations 때문에 오류 발생 임의로 들어가 스키마 삭제 후 다시 빌드 후 성공
## 6일차

- 토큰 인증 추가
- 스펙토랩 추가
- 회원가입 추가
- 로그인 추가
- 로그아웃 추가
- 회원정보 추가
- 회원정보 수정
- 회원정보 삭제

## 7일차

- 앱 구조 변경
- 상품 추가
- 상품 수정
- 상품 삭제
- 상품 조회
- 상품 상세 조회

## 8일차

- 주문 추가
- 주문 수정
- 주문 삭제
- 주문 조회
- 주문 상세 조회

## 9일차

- 주문 아이템 추가
- 주문 아이템 수정
- 주문 아이템 삭제
- 주문 아이템 조회
- 주문 아이템 상세 조회

## 10일차

- 주소 추가
- 주소 수정
- 주소 삭제
- 주소 조회
- 주소 상세 조회

### 추가 사항
    > 배포 버전 도커 및 aws 설정 하고 나서 추가 할 예정

 - 간단한 api만 넣어서 추후에 심오하게 바꿀 예정 
 - payment 추가 예정
 - TDD 적용 예정

## 11일차
 - 도커 배포
 - aws 설정
  - ec2 설정
  - ec2 shell 접속
  - 보안 그룹 인바인드 규칙 설정
  - 도커 설치
   > sudo apt-get update
   > sudo apt-get install -y docker.io
   > sudo apt install docker-compose
   - 도커 사용자 그룹 추가 (도커 down 하고 싶을 때)
     > sudo systemctl start docker
     > sudo usermod -aG docker $USER
     > ls -l /var/run/docker.sock
     > sudo chmod 666 /var/run/docker.sock
     > sudo reboot
  - git clone 후 docker-compose up -d 실행
   > clone 후 .env 파일 생성 후 환경변수 등록
   > docker-compose up -d 실행
   > docker ps 실행 후 정상적으로 실행되었는지 확인


## 기본 도커를 활용한 aws 배포 백엔드 프로젝트 완성

### 추가 사항
 - 간단한 api만 넣어서 추후에 심오하게 바꿀 예정 
 - payment 추가 예정
 - TDD 적용 예정
 - 도커 자동 빌드 예정 도커 CI 추가 예정
 - certbot 설정 예정 (https 적용)