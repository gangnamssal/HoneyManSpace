# Vue with DRF

----

## 1. Vue with DRF

- ### server & Client
  
  - **서버**
    
    - 클라이언트에게 **정보**와 **서비스**를 제공하는 컴퓨터 시스템
    
    - DB와 통신하며 데이터를 생성, 조회, 수정, 삭제를 담당한다.
    
    - 요청을 보낸 Client에게 정상적인 요청이었다면 처리한 결과를 응답한다.
  
  - **클라이언트**
    
    - **Server가 제공하는 서비스에 적절한 요청**을 통해 **Server로부터 반환 받은 응답을 사용자에게 표현**하는 기능



- ### Vue with DRF
  
  - **AJAX 요청 준비** 
    
    - 
      
      ![화면 캡처 2022-11-14 103114.png](C:\Users\multicampus\Desktop\home\필기\vue.js\화면%20캡처%202022-11-14%20103114.png)
    
    - 
      
      ![화면 캡처 2022-11-14 103139.png](C:\Users\multicampus\Desktop\home\필기\vue.js\화면%20캡처%202022-11-14%20103139.png)
    
    - 
      
      ![화면 캡처 2022-11-14 103622.png](C:\Users\multicampus\Desktop\home\필기\vue.js\화면%20캡처%202022-11-14%20103622.png) 

---

## 2. CORS

- ### Cross-Origin-Resource sharing
  
  - 위에서 브라우저가 요청을 보내고 서버의 응답이 브라우저에 도착했다. Server는 정상적으로 응답했지만 브라우저가 막은 것이다.
  
  - 보안상의 이유로 브라우저는 **동일 출처 정책(SOP)** 에 의해 다른 출처의 리소스와 상호작용 하는 것을 제한한다.



- ### SOP (Same - Origin Policy)
  
  - 동일 출처 정책
  
  - 불러온 문서나 스크립트가 다른 출처에서 가져온 리소스와 상호작용 하는 것을 제한하는 보안 방식이다.
  
  - 잠재적으로 해로울 수 있는 문서를 분리함으로써 공격받을 수 있는 경로를 줄인다.



- ### Origin - "출처"
  
  - **URL의 Protocol, Host, Port** 를 모두 포함하여 출처라고 부른다.
    
    - 
      
      ![화면 캡처 2022-11-14 104435.png](C:\Users\multicampus\Desktop\home\필기\vue.js\화면%20캡처%202022-11-14%20104435.png)
    
    - 
      
      ![화면 캡처 2022-11-14 104523.png](C:\Users\multicampus\Desktop\home\필기\vue.js\화면%20캡처%202022-11-14%20104523.png)



- ### CORS - 교차 출처 리소스 공유
  
  - 추가 **HTTP Header** 를 사용하여, 특정 출처에서 실행 중인 웹 어플리케이션이 **다른 출처의 자원에 접근할 수 있는 권한** 을 부여하도록 브라우저에 알려주는 체제
    
    - 어떤 출처에서 자신의 컨텐츠를 불러갈 수 있는지 **서버에 저장**할 수 있는 방법
  
  - **리소스가 자신의 출처와 다를 때 교차 출처 HTTP 요청을 실행**
    
    - 만약 다른 출처의 리소스를 가져오기 위해서는 이를 제공하는 서버가 브라우저에게 **다른 출처지만 접근해도 된다는 사실을 알려야한다.**





- ### CORS policy - 교차 출처 리소스 공유 정책
  
  - 다른 출처에서 온 리소스를 공유하는 것에 대한 정책
  
  - CORS policy에 위배되는 경우 브라우저에서 해당 응답 결과를 사용하지 않는다.
    
    - Server에서 응답을 주더라도 브라우저에서 거절한다.
  
  - 다른 출처의 리소스를 불러오려면 그 출처에서 **올바른 CORS header**를 포함한 응답을 반환해야 한다.



- ### How to set CORS
  
  - CORS 표준에 의해 추가된 HTTP Response Header를 통해 이를 통제 가능하다.
  
  - 
    
    ![화면 캡처 2022-11-14 105814.png](C:\Users\multicampus\Desktop\home\필기\vue.js\화면%20캡처%202022-11-14%20105814.png)
  
  - **Access-Control-Allow-Origin**
    
    - 단일 출처를 지정하여 브라우저가 해당 출처가 리소스에 접근하도록 허용한다.



- ### django-cors-headers library 사용하기
  
  - django-cors-headers github에서 내용 확인
  
  - **응답에 CORS header를 추가** 해주는 라이브러리
  
  - 다른 출처에서 Django 애플리케이션에 대한 브라우저 내 요청을 허용한다.
    
    - 
      
      ![화면 캡처 2022-11-14 110043.png](C:\Users\multicampus\Desktop\home\필기\vue.js\화면%20캡처%202022-11-14%20110043.png)
    
    - 
      
      ![화면 캡처 2022-11-14 110237.png](C:\Users\multicampus\Desktop\home\필기\vue.js\화면%20캡처%202022-11-14%20110237.png)
      
      - 
        
        ![화면 캡처 2022-11-14 110320.png](C:\Users\multicampus\Desktop\home\필기\vue.js\화면%20캡처%202022-11-14%20110320.png)
      
      - 
        
        ![화면 캡처 2022-11-14 110418.png](C:\Users\multicampus\Desktop\home\필기\vue.js\화면%20캡처%202022-11-14%20110418.png)

---



## 3. DRF Auth System

- ### Authentication & Authorization
  
  - **Authentication**
    
    - 인증, 입증
    
    - 모든 보안 프로세스의 첫 번째 단계 (가장 기본 요소)
    
    - **401 Unauthorized**
      
      - 비록 HTTP 표준에서는 '미승인'을 명확히 하고 있지만, 의미상 이 응답은 비인증을 의미한다.
  
  - **Authorization**
    
    - 권한 부여, 허가
    
    - 사용자에게 특정 리소스 또는 기능에 대한 액세스 권한을 부여하는 과정 (절차)
    
    - **보안 환경에서 권한 부여는 항상 인증이 먼저 필요하다.**
    
    - **403 Forbidden**
      
      - 401과 다른 점은 서버는 클라이언트가 누구인지 알고 있다.



- ### 인증 여부 확인 방법
  
  - **DRF 공식 문서에서 제안하는 인증 절차 방법**
    
    - 
      
      ![화면 캡처 2022-11-14 111231.png](C:\Users\multicampus\Desktop\home\필기\vue.js\화면%20캡처%202022-11-14%20111231.png)
    
    - 우리가 사용할 방법은 DRF가 기본으로 제공해주는 인증 방식 중 하나인 **TokenAuthentication**
    
    - 모든 상황에 대한 인증 방식을 정의하는 것이므로, 각 요청에 따라 다른 인증 방식을 거치고자 한다면 다른 방식이 필요하다.
    
    - 
      
      ![화면 캡처 2022-11-14 111500.png](C:\Users\multicampus\Desktop\home\필기\vue.js\화면%20캡처%202022-11-14%20111500.png)



- ### 다양한 인증 방식
  
  - 
    
    ![화면 캡처 2022-11-14 111551.png](C:\Users\multicampus\Desktop\home\필기\vue.js\화면%20캡처%202022-11-14%20111551.png)
  
  - 
    
    ![화면 캡처 2022-11-14 111600.png](C:\Users\multicampus\Desktop\home\필기\vue.js\화면%20캡처%202022-11-14%20111600.png)



- ### TokenAuthentication 사용 방법
  
  - 
    
    ![화면 캡처 2022-11-14 111659.png](C:\Users\multicampus\Desktop\home\필기\vue.js\화면%20캡처%202022-11-14%20111659.png)
  
  - 
    
    ![화면 캡처 2022-11-14 111707.png](C:\Users\multicampus\Desktop\home\필기\vue.js\화면%20캡처%202022-11-14%20111707.png)
  
  - 
    
    ![화면 캡처 2022-11-14 111717.png](C:\Users\multicampus\Desktop\home\필기\vue.js\화면%20캡처%202022-11-14%20111717.png)



- ### django-rest-auth / dj-rest-auth
  
  - 회원가입, 인증(소셜미디어 인증 포함), 비밀번호 재설정, 사용자 세부 정보 검색, 회원 정보 수정 등을 위한 REST API end point 제공
  
  - 
    
    ![화면 캡처 2022-11-14 111920.png](C:\Users\multicampus\Desktop\home\필기\vue.js\화면%20캡처%202022-11-14%20111920.png)



- ### dj-rest-auth 사용 방법
  
  - 
    
    ![화면 캡처 2022-11-14 112025.png](C:\Users\multicampus\Desktop\home\필기\vue.js\화면%20캡처%202022-11-14%20112025.png)
  
  - 
    
    ![화면 캡처 2022-11-14 112304.png](C:\Users\multicampus\Desktop\home\필기\vue.js\화면%20캡처%202022-11-14%20112304.png)



- ### Registration
  
  - Registration 기능을 사용하기 위해 추가 기능 등록 및 설치가 필요하다.
    
    - dj-rest-auth는 소셜 회원가입을 지원한다.
    
    - dj-rest-auth의 회원가입 기능을 사용하기 위해서는 **django-allauth**가 필요하다.
  
  - 
    
    ![화면 캡처 2022-11-14 112546.png](C:\Users\multicampus\Desktop\home\필기\vue.js\화면%20캡처%202022-11-14%20112546.png)
  
  - 
    
    ![화면 캡처 2022-11-14 112647.png](C:\Users\multicampus\Desktop\home\필기\vue.js\화면%20캡처%202022-11-14%20112647.png)
    
    - **SITE_ID**
      
      - Django는 하나의 컨텐츠를 기반으로 여러 도메인에 컨텐츠를 게시 가능하도록 설계되었다.
      
      - 다수의 도메인이 하나의 데이터베이스에 등록
      
      - 현재 프로젝트가 첫번째 사이트임을 나타낸다.
  
  - 
    
    ![화면 캡처 2022-11-14 113023.png](C:\Users\multicampus\Desktop\home\필기\vue.js\화면%20캡처%202022-11-14%20113023.png)
  
  - 
    
    ![화면 캡처 2022-11-14 121742.png](C:\Users\multicampus\Desktop\home\필기\vue.js\화면%20캡처%202022-11-14%20121742.png)



- ### Password change
  
  - 
    
    ![화면 캡처 2022-11-14 133106.png](C:\Users\multicampus\Desktop\home\필기\vue.js\화면%20캡처%202022-11-14%20133106.png)
  
  - 
    
    ![화면 캡처 2022-11-14 133239.png](C:\Users\multicampus\Desktop\home\필기\vue.js\화면%20캡처%202022-11-14%20133239.png)
  
  - **확인**
    
    - 
      
      ![화면 캡처 2022-11-14 133331.png](C:\Users\multicampus\Desktop\home\필기\vue.js\화면%20캡처%202022-11-14%20133331.png)
    
    - 
      
      ![화면 캡처 2022-11-14 133422.png](C:\Users\multicampus\Desktop\home\필기\vue.js\화면%20캡처%202022-11-14%20133422.png)



- ### Permission setting
  
  - 권한 설정 방법 확인
    
    - DRF 공식 문서 > API Guide > Permissions 확인
  
  - 권한 세부 설정
    
    1. 모든 요청에 대해 인증을 요구하는 설정
    
    2. 모든 요청에 대해 인증이 없어도 허용하는 설정
  
  - 설정 위치 == 인증 방법을 설정한 곳과 동일하다.
    
    - 
      
      ![화면 캡처 2022-11-14 133610.png](C:\Users\multicampus\Desktop\home\필기\vue.js\화면%20캡처%202022-11-14%20133610.png)
    
    - 
      
      ![화면 캡처 2022-11-14 133640.png](C:\Users\multicampus\Desktop\home\필기\vue.js\화면%20캡처%202022-11-14%20133640.png)
  
  - 인증된 경우만 허용하도록 권한 부여 
    
    - 
      
      ![화면 캡처 2022-11-14 133743.png](C:\Users\multicampus\Desktop\home\필기\vue.js\화면%20캡처%202022-11-14%20133743.png)
  
  - 

## 4. DRF Auth with Vue

## 5. DRF- spectacular
















































































