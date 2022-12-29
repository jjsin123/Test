# 프로젝트(웹 사이트 구축)

---

![%EC%9B%B9%EC%82%AC%EC%9D%B4%ED%8A%B8](https://user-images.githubusercontent.com/114375741/209914051-bebb22f2-4426-45ef-857b-ba01465628aa.jpg)


### 프로젝트 기획 동기

---

- 미니 프로젝트에 이은 두번째 프로젝트로 Python, Django를 기반으로 웹사이트를 처음부터 끝까지 제작해 보고 싶어져서 프로젝트를 진행해 보았다 .
- 주요 기능으로 게시판, 블로그, 실시간 채팅, 회원가입, 로그인 기능들을 구현해보고 싶었고 추가적으로 대문페이지와,  자기소개 페이지를 마련해서 포트폴리오도 담아 보았다.
- UI 디자인적 요소보다 기능 구현면에 초점을 두고 개발을 진행하였다.

### 깃허브 & 도메인

---

- 깃허브 : [https://github.com/jjsin123/Test](https://github.com/jjsin123/Test)
- 도메인 : [https://project-mjgjc.run.goorm.io](https://project-mjgjc.run.goorm.io/)

### 기술 및 개발 환경

---

- 사용 언어 : Python , HTML, CSS, JavaScript
- 웹 프레임워크 : Django
- 서버 : Nginx
- DB : SQLite3
- 버전 관리 : git
- 기타 모듈 : channels, markdownx, crispy_forms, Redis
- 사용 툴 : goormIDE, Pycharm, google OAuth Client, cmder, docker

### 개발 기간

---

- 개발기간 : 2022.11~12

### 시스템 구성도

---

![Web_%EC%8B%9C%EC%8A%A4%ED%85%9C_%EA%B5%AC%EC%84%B1%EB%8F%84_%EC%B5%9C%EC%A2%85](https://user-images.githubusercontent.com/114375741/209914096-ab853c2c-4dc8-47c8-98bc-a522f27638f3.jpg)

### ER 다이어그램

---

![django_erd](https://user-images.githubusercontent.com/114375741/209914125-d85949ab-0bd9-4e2c-9004-243573bd3286.png)

### 기능 설명

---

- 회원가입 (email 가입, google연동 가입)
- 로그인
- 블로그 페이지
    - Create Post (로그인 한 회원에 한해서 Create 버튼 출력 됨, 이미지 또는 파일 업로드 가능, 이미지를 업로드 하지 않을 시 무작위 이미지를 생성 후 적용, Post 내용은 MarkDown형식으로 입출력 가능, 카테고리 추가, 태그 추가 가능, 등록시 자동으로 작성자, 작성시간 출력, 뒤로가기 버튼 출력)
    - Edit Post (Post를 등록한 회원에 한해서 Edit 버튼 출력, 기능은 Create와 동일)
    - Delete Post (Post를 등록한 회원에 한해서 Delete 버튼 출력, Post 삭제-삭제 시 정말 삭제 할 것인지 확인 창 출력)
    - Comment (회원에 한해서 작성가능, 비회원일시 Log in and Leave a Comment 문구 출력 후 로그인 창으로 이동, 댓글 작성자에 한 해서 댓글 수정, 삭제버튼 출력, 삭제 시 정말 삭제 할 것인지 확인 창 출력)
    - 그 외의 기능 : 카테고리(추가,삭제), 태그(추가,삭제), Post검색(제목, 태그로 검색 가능), 한 페이지당 포스트 5개씩 등록가능, 초과시 이전,다음 페이지 페이징 네이션가능
- 게시판 페이지
    - 글쓰기 (로그인 한 회원에 한해서 글쓰기 버튼 출력 됨, 글 내용은 MarkDown형식으로 입출력 가능, 등록시 자동으로 작성자, 작성시간 출력, 게시글 작성 후 뒤로가기 버튼 출력)
    - 게시글 수정 (게시글을 작성 한 회원에 한해서 게시글 수정 버튼 출력, 기능은 글쓰기와 동일)
    - 게시글 삭제 (게시글을 등록한 회원에 한해서 게시글 삭제 버튼 출력, 게시글 삭제 시 정말 삭제 할 것인지 확인 창 출력)
    - 댓글 남기기 (회원에 한해서 작성가능, 비회원일시 로그인 후 댓글을 남겨보세요 문구 출력 후 로그인 창으로 이동, 댓글 작성자에 한 해서 댓글 수정, 삭제버튼 출력, 삭제 시 정말 삭제 할 것인지 확인 창 출력)
    - 그 외의 기능 : 한 페이지당 게시글 10개씩 등록가능, 초과시 이전,다음 페이지 페이징네이션 가능
- 실시간채팅(Channels)
    - 채팅방 생성
    - 입장한 채팅방에서 실시간 채팅 이용
    - 현재 오류 발생하여 수정 중

### 실행 화면

---

✅ 대문 페이지

![%EB%8C%80%EB%AC%B8%ED%8E%98%EC%9D%B4%EC%A7%80](https://user-images.githubusercontent.com/114375741/209914165-a46972fc-40b6-460d-b5e7-e12d43c30d21.png)

1. navbar 2. 관리자 권한이 있는 계정은 Admin 버튼 출력 3. 비회원이면 Login 버튼, 회원이면 계정명 출력 4. 대문 소개 문구 5. 최근 블로그 Post 미리보기 6. footer

✅ Blog List 페이지

![%EB%B8%94%EB%A1%9C%EA%B7%B8%EB%A6%AC%EC%8A%A4%ED%8A%B8%ED%8E%98%EC%9D%B4%EC%A7%80](https://user-images.githubusercontent.com/114375741/209914203-86d6d2bc-42e0-4bf9-ba51-01c369d603c0.png)

1. 회원 계정일시 New Post 버튼 출력 2. 검색 기능(글 제목, Tag로 검색) 3. 카테고리 사이드바 4. Post 상세 보기 버튼

✅ Create Post 페이지

![CreatePost%ED%8E%98%EC%9D%B4%EC%A7%80](https://user-images.githubusercontent.com/114375741/209914257-b389bb68-d0ce-4737-a7cf-cf72a3c5149b.png)

✅ Blog datail 페이지

![%EB%B8%94%EB%A1%9C%EA%B7%B8%EB%94%94%ED%85%8C%EC%9D%BC%ED%8E%98%EC%9D%B4%EC%A7%801](https://user-images.githubusercontent.com/114375741/209914224-4dd0deb7-bada-421a-9b93-d8c9b1425751.png)

✅ ****************Board List

![boardlist](https://user-images.githubusercontent.com/114375741/209914276-4794f344-f960-4f39-895b-e6c815553416.png)

✅ Board Detail 페이지

![boarddetail](https://user-images.githubusercontent.com/114375741/209914288-0c9c802f-cd00-4d8e-8882-9e385bb408b2.png)

✅ Chat 페이지

Nginx로 사용시 문제가 발생하여 수정 중 추후 업로드 예정

✅ About me 페이지

![aboutme](https://user-images.githubusercontent.com/114375741/209914302-fdc1f760-5aa4-402e-8765-b52fb4470bbb.png)

### 라이센스

---

“This project is licensed under the terms of the **GNU General Public License v3.0** license.”

**[GNU General Public License v3.0](https://github.com/jjsin123/Test/blob/add-license-1/LICENSE)**

### 기여자 정보

---

신종규

- 깃허브 : [@jjsin123](https://github.com/jjsin123)
- 이메일 : jjsin123@naver.com
