# 블로그

### 사용한 기술
* Front-End : CSS, HTML, Bootstrap
* Database : mysql 8.x, redis
* Language : Python 3.8
* Framework : django 4.0

### api
### git flow
* master, develop, feature, hotfix, release
* 개발 단계 : feature 개발 후, develop에서 관리

### 테이블 설계
* post : 글 정보
* comment : 글에 대한 댓글 정보
* post <-> comment (양방향)[1tom]

### 로그인, 로그아웃
* 장고 관리자(superuser)를 사용
* 로그인, 로그아웃 가능

### post 관리
* post 생성, 수정, 삭제
* post list

### comment 관리
* comment 생성, 수정, 삭제
* comment list 

### references
* https://tutorial.djangogirls.org/ko/django_start_project/
* https://tutorial-extensions.djangogirls.org/ko
* https://docs.djangoproject.com/en/4.0/