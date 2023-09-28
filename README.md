# Night Watch Server

## Quick Start (개발 서버)

1. mariadb 접속 및 database 생성

   ```
   mariadb -uroot -p
   ```

   ```
   CREATE DATABASE nightwatch;
   ```

2. 프로젝트 루트에 `.env`파일 추가 후, 다음 환경변수를 작성

   ```
   MARIADB_HOST=127.0.0.1
   MARIADB_PORT=3306
   MARIADB_DATABASE=nightwatch
   MARIADB_USER=root
   MARIADB_PASSWORD=0000 #root password
   MARIADB_ROOT_PASSWORD=0000 #처음 설치 시 입력했던 root password 입력
   ```

3. 가상환경 생성 및 활성화

   ```
   python3 -m venv .venv
   ```

   window

   ```
   source .venv/Scripts/activate.bat
   ```

   mac

   ```
   source .venv/bin/activate
   ```

4. requirements.txt로 패키지 설치

   ```
   pip install -r requirements.txt
   ```

5. 개발 서버 실행
   ```
   uvicorn app.main:app --reload
   ```
