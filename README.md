# DA-35-5th-KKL-Hocance

## 1. 프로젝트 이름
   * 호캉스 : 호텔 업체의 자사 호텔 리뷰 및 평점을 효율적으로 관리하는 시스템

## 2. 프로젝트 주제 간단한 소개
   * 자사 호텔의 리뷰 데이터를 통합관리시스템

## 3. 팀원과 담당업무
   1. 김주화 : 게시판 app, 리뷰 업로드 데이터 게시판 app 시각화?
   2. 이주호 : 로그인 app, home app
   3. 김연중 : 차트 app, 리뷰 업로드 app

## 4. 산출물 파일링크
    * https://github.com/Playdata-G-DA35/DA-35-5th-__-review.git

## 5. 요구사항 명세서

| 요구사항 ID | 기능유형 | 요구사항 명                  | 요구사항 내용                                                                                                     | 중요도 | 담당자 | 요청자 | 수용여부 |
|-------------|----------|-----------------------------|------------------------------------------------------------------------------------------------------------------|--------|--------|--------|----------|
| REQ--001    | 기능     | 메인화면 정보 공개 제한     | 로그인을 하지 않은 상태에서는 메인 화면의 사이드바를 숨겨 정보 공개를 제한합니다.                                   | 상     | 이주호 | 이주호 | 수용     |
| REQ--002    | 기능     | 회원가입                    | 회원가입 시 아이디에 제한된 특수문자만 허용하고, 비밀번호는 최소 8자리 이상이며 숫자로만 이루어지지 않도록 제한합니다.   | 상     | 이주호 | 이주호 | 수용     |
| REQ--003    | 기능     | 로그인 완료 시 홈화면 이동 | 로그인 버튼을 누르면 로그인 화면으로 이동하며, 로그인 성공 시 홈화면으로 이동합니다.                              | 상     | 이주호 | 이주호 | 수용     |
| REQ--004    | 기능     | 로그아웃 시 확인 절차       | 로그아웃 시 확인 절차를 추가하여, 사용자가 정말 로그아웃할 것인지 묻고, 확인(True) 시 로그아웃 후 초기화면으로 이동합니다. | 중     | 이주호 | 이주호 | 수용     |
| REQ--005    | 기능     | 상단 및 사이드 네비게이션바 | 네비게이션바에서 로그인, 로그아웃 및 원하는 기능으로 이동할 수 있는 화면을 제공하며, 로고를 누르면 홈화면으로 이동할 수 있어야 합니다. | 상     | 이주호 | 이주호 | 수용     |
| REQ--006    | 기능     | 리뷰 평점 차트 시각화       | 리뷰 데이터의 평점을 일별로 웹사이트에 시각화하며, 사용자가 기간을 설정할 수 있어야 합니다.                           | 상     | 김연중 | 김연중 | 수용     |
| REQ--007    | 기능     | 리뷰 긍정, 부정 차트 시각화 | 리뷰 데이터를 일별 막대 그래프로 표현하고, 긍정과 부정 비율을 시각화하며, 사용자가 기간을 설정할 수 있어야 합니다.      | 상     | 김연중 | 김연중 | 수용     |
| REQ--008    | 기능     | 리뷰 주제 차트 시각화       | 리뷰 데이터의 내용을 분석하여 웹사이트에 빈도가 높은 주제를 시각화합니다.                                            | 중     | 김연중 | 김연중 | 반려     |
| REQ--009    | 기능     | 리뷰 데이터 업로드          | 리뷰 데이터를 웹사이트 내에서 업로드하는 화면을 구현합니다.                                                       | 상     | 김연중 | 김연중 | 수용     |
| REQ--010    | 비기능   | 리뷰 데이터 저장            | 리뷰 데이터를 웹사이트 내에서 업로드하면 DB에 저장되도록 구현합니다.                                                | 상     | 김연중 | 김연중 | 수용     |
| REQ--011    | 기능     | 리뷰 업로드 성공 팝업창     | 리뷰 업로드가 성공하면 팝업으로 성공 알람을 제공합니다.                                                            | 중     | 이주호 | 이주호 | 수용     |
| REQ--012    | 기능     | 리뷰 데이터 게시판          | 리뷰 데이터의 일자, 평점, 내용, 긍/부정 데이터를 게시판 화면에 제공합니다.                                           | 상     | 김주화 | 김주화 | 수용     |
| REQ--013    | 기능     | 리뷰 데이터 게시판 상세 설정 | 리뷰 데이터 콘텐츠가 길어질 경우 리뷰를 클릭하면 상세페이지로 연결되는 화면을 제공합니다.                             | 중     | 김주화 | 김주화 | 수용     |
| REQ--014    | 비기능   | 리뷰 데이터 연결            | DB에 저장된 리뷰 데이터를 읽어와서 게시판에서 요구하는 컬럼들의 데이터를 제공합니다.                                  | 상     | 김주화 | 김주화 | 수용     |




## 6. 화면설계서

* [화면설계서](https://github.com/Playdata-G-DA35/DA-35-5th-KKL-Hocance/blob/main/%ED%99%94%EB%A9%B4%EC%84%A4%EA%B3%84%EC%84%9C.md) </br>

## 7. 어플리케이션 설계서

### 7-1. 데이터베이스 정의서

#### 1) 사용자 정보 테이블

- **테이블명 : auth_user**
- 테이블 설명 : 사용자 정보를 저장하는 테이블 
- 컬럼 정보

### 테이블: [테이블 이름]

| 번호 | 컬럼명       | 데이터 타입  | Not Null | 기본값 | Primary Key |
| ---- | ------------ | ------------ | -------- | ------- | ----------- |
| 0    | id           | INTEGER      | Yes      | None    | Yes         |
| 1    | password     | VARCHAR(128) | Yes      | None    | No          |
| 2    | last_login   | DATETIME     | No       | None    | No          |
| 3    | is_superuser | BOOL         | Yes      | None    | No          |
| 4    | username     | VARCHAR(150) | Yes      | None    | No          |
| 5    | last_name    | VARCHAR(150) | Yes      | None    | No          |
| 6    | email        | VARCHAR(254) | Yes      | None    | No          |
| 7    | is_staff     | BOOL         | Yes      | None    | No          |
| 8    | is_active    | BOOL         | Yes      | None    | No          |
| 9    | date_joined  | DATETIME     | Yes      | None    | No          |
| 10   | first_name   | VARCHAR(150) | Yes      | None    | No          |


#### 2) 리뷰 데이터 정보 테이블

- **테이블명 : review_upload_review**
- 테이블 설명 : 리뷰의 평점, 내용, 일자, 긍/부정 정보를 저장하는 테이블 
- 컬럼 정보

| 번호 | 컬럼명   | 데이터 타입   | Not Null | 기본값 | Primary Key |
| ---- | -------- | ------------- | -------- | ------- | ----------- |
| 0    | id       | INTEGER       | Yes      | None    | Yes         |
| 1    | review   | TEXT          | Yes      | None    | No          |
| 2    | rating   | INTEGER       | Yes      | None    | No          |
| 3    | date     | DATE          | Yes      | None    | No          |
| 4    | sentiment| VARCHAR(10)   | Yes      | None    | No          |

### 7-2. 프로그램 파일 목록

| NO  | 단위업무명        | App              | 이름                  | 프로그램분류 | 프로그램타입 | 위치                             |
|-----|-------------------|------------------|-----------------------|--------------|--------------|----------------------------------|
| 1   | 회원관리          | accounts         | LOGIN                 | Template     | template     | accounts/templates/accounts      |
| 2   |                   |                  | LOGOUT                | Template     | template     | accounts/templates/accounts      |
| 3   |                   |                  | signup.html           | Template     | template     | accounts/templates/accounts      |
| 4   |                   |                  | signup                | view         | function     | accounts/views.py                |
| 5   | 사이드 내비게이션바 | myapp            | home_view             | view         | function     | myapp/views.py           |
| 6   |                   |                  | home.html             | Template     | template     | mysite/templates         |
| 7   | 평점차트           | chart            | rating_chart          | View         | function     | chart/views.py            |
| 8   |                   |                  | chart.html            | Template     | template     | mysite/templates          |
| 9   |                   |                  | DateRangeForm         | forms        | function     | chart/forms.py            |
| 10  | 메인화면           | page             | home                  | View         | function     | pages/views.py            |
| 11  |                   |                  | home.html             | Template     | template     | pages/templates           |
| 12  | 리뷰게시판         | polls            | ReviewAdmin           | admin        | function     | polls/admin.py            |
| 13  |                   |                  | ReviewForm            | form         | function     | polls/form.py             |
| 14  |                   |                  | board                 | function     | function     | polls/views.py            |
| 15  |                   |                  | read                  | function     | function     | polls/views.py            |
| 16  |                   |                  | board.html            | Template     | template     | polls/templates/polls     |
| 17  |                   |                  | read.html             | Template     | template     | polls/templates/polls     |
| 18  | 리뷰 업로드        | REVIVEW_UPLOAD   | ReviewUploadForm      | form         | form         | review_upload/forms.py    |
| 19  |                   |                  | Review                | models       | function     | review_upload/models.py   |
| 20  |                   |                  | upload_review         | View         | view         | review_upload/views.py    |
| 21  |                   |                  | upload_review.html    | Template     | template     | mysite/templates          |
| 22  |                   |                  | upload_success.html   | Template     | template     | mysite/templates   |



## 10. 최종 보고서

### 10-1) 프로젝트 주제

* 자사 호텔의 리뷰 데이터를 통합관리시스템에 업로드
* 자사 호텔 리뷰를 효율적으로 관리하고 고객의 의견을 기반 서비스 개선 및 기획
* 자사 호텔의 평판(리뷰, 평점, 긍정/부정) 일별로 확인하여 자사 호텔의 위기관리

### 10-2) 프로젝트 목적(선택 이유)

* 비즈니스 환경에서 본사는 여러 지점을 운영하는 경우가 많다. 각 지점에서 수집되는 고객 의견을 한 곳에서 효율적으로 관리하는 일은 매우 중요한 과제이지만 각 지점의 리뷰 데이터를 수동으로 수집하고 분석하는 것은 시간과 자원이 많이 소모되며, 데이터의 일관성과 신뢰성을 확보하기에 한계가 있다.

* 이 프로젝트의 주요 목적는 각 지점에서 수집되는 리뷰 데이터를 통합 관리 시스템에 저장하고, 본사 직원들이 지점별 고객 의견을 효과적으로 확인하고 개선할 수 있도록 하는 시스템을 구축하는 것이다. 이를 통해 고객의 의견을 반영하여 새로운 서비스를 기획하거나 기존 서비스를 개선하는 과정을 효율적으로 수행 할 수 있다.

### 10-3) 프로젝트 도중 발생했던 문제 및 해결방식

* **권한없는 사용자 정보 전달 제한**
  * 홈화면을 따로 구현하고 로그인을 하지 않는다면 접근하지 못하도록 웹 화면 구현
* **웹사이트 크롤링**
  * 웹사이트 크롤링을 하여 특정 호텔의 리뷰를 가져오려 했으나, 자동화된 접근을 막아 호텔 리뷰 데이터셋 활용
  * 해당 데이터 셋은 리뷰 내용, 별점만 가지고 있으나 구현하려고 하는 웹사이트는 일자, 긍/부정 등의 데이터를 예시로 보여주고자하여 임의로 데이터를 넣어 활용
* **chart 구현**
  * chart를 구현하는 다양한 방법을 시도했으나, 오류가 지속적으로 발생
  * 가장 기본적인 방법인 matplotlib을 활용해 이미지를 저장하고 웹사이트에 해당 이미지를 보여주는 방식으로 차트를 구현
* **업로드된 review데이터를 게시판 화면에 구현**
  * 리뷰가 review_upload_review라는 테이블로 db에 저장이 되었으나, 게시판에 해당 데이터를 시각화하는 부분에서 한계발생
  * admin에 review_upload_review 데이터 연결하여 admin 페이지에서는 리뷰 데이터가 확인이됐지만 실제 웹화면에서는 구현이 안됨
  * views.py, urls.py, board.html 수정하여 데이터 게시판 화면에 제공

### 10-4) 프로젝트 차후 업그레이드 계획
* **주제 분석을 통한 차트 개선**
	* 리뷰 데이터를 주제별로 분석하여 차트에 반영. 
	자연어 처리(NLP) 기술을 활용해 리뷰 내용을 주제별로 분류하고, 각 주제에 대한 리뷰 수, 평점, 긍정/부정 비율 등을 시각화

* **리뷰 내용 전처리 및 불필요한 내용 제거**
	* 불필요한 공백 및 특수 문자 제거: 텍스트에서 불필요한 공백, 특수 문자 등을 제거
	* 오타 수정 및 정규화: 일반적으로 발생하는 오타를 수정 및 동일한 의미를 가지는 단어를 정규화
	* 중복 리뷰 제거: 동일한 사용자가 여러 번 작성한 중복 리뷰를 제거
	* 스팸 리뷰 필터링: 자동화된 스팸 리뷰를 필터링

* **게시판 정렬 기능 추가**
	* 게시판에서 리뷰를 날짜, 별점, 긍정/부정 기준으로 정렬할 수 있는 기능을 추가할 예정
	* 날짜별 정렬, 별점별 정렬 긍/부정 정렬
