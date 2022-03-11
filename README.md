# 블로그

### 사용한 기술
* Front-End : CSS, HTML, Bootstrap
* Database : mysql 8.x, redis
* Language : Python 3.8
* Framework : django 4.0

### api
1. 포스트 리스트
* url : GET /
* request : 
* response : blog/post_list.html

2. 포스트 상세
* url : GET /post/id
* request :
 
        { 
            "id": 2 
        }
* response : blog/post_detail.html

3. 포스트 생성 폼
* url : GET /post/new
* request :
* response : blog/post_edit.html

4. 포스트 생성
* url : POST /post/new
* request :
 
        { 
            "postForm":
                "title": "dexter", 
                "text": "dexter register!" 
        }
* response : blog/post_edit.html

5. 포스트 수정 폼
* url : GET /post/id/edit
* request :
 
        { 
            "id": 2 
        }
* response : blog/post_edit.html

6. 포스트 수정
* url : POST /post/id/edit
* request :
 
        { 
            "id": 2 
        }
* response : blog/post_edit.html

7. 포스트 초안 리스트
* url : GET /drafts
* request :
* response : blog/post_draft_list.html

8. 포스트 초안 출판
* url : GET /post/id/publish
* request :
 
        { 
            "id": 2 
        }
* response : blog/post_detail.html

9. 포스트 삭제
* url : POST /post/id/remove
* request :
 
        { 
            "id": 2 
        }
* response : blog/post_detail.html

10. 댓글 추가 폼
* url : GET /post/id/comment
* request :
 
        { 
            "id": 2 
        }
* response : blog/add_comment_to_post.html

11. 댓글 추가
* url : POST /post/id/comment
* request :
 
        { 
            "id": 2, 
            "commentForm": 
                "author": "dex", 
                "text": "good!" 
        }
* response : blog/add_comment_to_post.html

12. 댓글 승인
* url : POST /comment/id/approve
* request :
 
        { 
            "id": 2
        }
* response : blog/post_detail.html

13. 댓글 삭제
* url : POST /comment/id/remove
* request :
 
        { 
            "id": 2
        }
* response : blog/post_detail.html

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
* 포스트 생성, 수정, 삭제, 초안 출판
* 포스트 리스트, 포스트 초안 리스트

### comment 관리
* comment 생성, 승인, 삭제
* comment 리스트 

### references
* https://tutorial.djangogirls.org/ko/django_start_project/
* https://tutorial-extensions.djangogirls.org/ko
* https://docs.djangoproject.com/en/4.0/