# ITSAC 2.0

## 1) 개발환경 셋팅
* python3 및 pip3 설치 - [링크](https://www.python.org/)
* virtualenv 설치 : "pip3 install virtualenv" <br/>
 (SSL 인증 오류시 : "pip3 --trusted-host pypi.org --trusted-host files.pythonhosted.org install virtualenv")
  * 가상환경 셋팅 : "virtualenv venv"
    * Windows : "call .\venv\Script\activate
    * Linux/Mac : "source ./venv/bin/activate"
  * 가상환경 django 프레임워크 설치 > "pip3 install django" <br/>
     (SSL 인증 오류시 : "pip3 --trusted-host pypi.org --trusted-host files.pythonhosted.org install django")
    
* * *

## 2) 동작 스크립트
**※ 가상환경에서 실행**
* 서버 실행 : python3 manage.py runserver
