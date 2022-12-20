# JavaScript 심화

## 1. DOM

- ### Browser APIs

  - 웹 브라우저에 내장된 API로 현재 컴퓨터 환경에 관한 데이터를 제공하거나 여러가지 유용하고 복잡한 일을 수행
  - **종류**
    - DOM
    - Geolocation API - 지리정보 API
    - WebGL - 그래픽 API



- ### DOM

  - 문서 객체 모델 (Document Object Model)
  - **문서의 구조화된 표현을 제공하며 프로그래밍 언어가 DOM 구조에 접글할 수 있는 방법을 제공**
    - 문서 구조, 스타일, 내용 등을 변경할 수 있게 도움을 준다
    - HTML 콘텐츠를 추가, 제거, 변경하고, 동적으로 페이지에 스타일을 추가하는 등 HTML / CSS를 조작할 수 있다.
  - 문서가 구조화되어 있으며 각 요소는 객체(object)로 취급한다.
  - 단순한 속성 접근 , 메서드 활용 뿐만 아니라 프로그래밍 언어적 특성을 활용한 조작이 가능하다.
  - DOM은 문서를 논리 트리로 표현한다.
  - DOM 메서드를 사용하면 프로그래밍적으로 트리에 접근할 수 있고 이를 통해 문서의 구조, 스타일, 컨텐츠를 변경할 수 있다.
  - ![화면 캡처 2022-10-24 112801](C:.\화면 캡처 2022-10-24 112801.png)
  - DOM은 웹 페이지의 객체 지향 표현이며, 스크립트 언어를 이용해 DOM을 수정할 수 있다.
  - 모든 웹 브라우저는 스크립트 언어가 접근할 수 있는 웹페이지를 만들기 위해 DOM을 항상 사용한다.



- ### DOM의 주요 객체

  - **window**
  - **document**
  - **navigator, location, history, screen ...**



- ### window Object

  - DOM을 표현하는 창
  - 가장 최상위 객체 (**작성 시 생략 가능**)
  - 탭 기능이 있는 브라우저에서는 각각의 탭을 각각의 window 객체로 나타낸다.
  - ![화면 캡처 2022-10-24 113417](C:.\화면 캡처 2022-10-24 113417.png)



- ### document Object

  - **브라우저가 불러온 웹 페이지 전체를 의미한다.**
  - 페이지 컨텐츠의 진입점 역할을 하며, <body>등과 같은 수 많은 다른 요소들을 포함하고 있다.
  - **document는 window의 속성이다. 즉, window는 생략이 가능하다.**



- ### 파싱 (Parsing)

  - 구문 분석, 해석
  - 브라우저가 문자열을 해석하여 DOM Tree로 만드는 과정
  - ![화면 캡처 2022-10-24 130209](C:.\화면 캡처 2022-10-24 130209.png)



- ### DOM 조작

  - **DOM 조작 순서**

    1. **선택 (Select)**
       - **선택 관련 메서드**
         1. **document.querySelector(selector)**
            - 제공한 선택자와 일치하는 **element 한 개 선택**
            - 제공한 CSS selector를 만족하는 **첫 번째 element 객체를 반환** (없다면 null 반환)
         2. **document.querySelectorAll(selector)**
            - 제공한 선택자와 일치하는 **여러 element를 선택**
            - 매칭 할 하나 이상의 셀렉터를 포함하는 **유효한 CSS selector를 인자(문자열)로 받음**
            - 제공한 CSS selector를 만족하는 **NodeList를 반환**
              - **NodeList**
                - index로만 각 항목에 접근 가능
                - 배열의 forEach 메서드 및 다양한 배열 메서드 사용 가능
                - **querySelectorAll()에 의해 반환되는 NodeList는 DOM의 변경사항을 실시간으로 반영하지 않는다.**
    2. **조작 (Manipulation)**
       - **생성**
         - **ducument.createElement(tagName)**
           - 작성한 tagName의 HTML 요소를 생성하여 반환
       - **입력**
         - **Node.innerText**
           - Node 객체와 그 자손의 텍스트 컨텐츠(DOMString)를 표현 (해당 요소 내부의 raw text)
           - 사람이 읽을 수 있는 요소만 남김
           - 줄 바꿈을 인식하고 숨겨진 내용을 무시하는 등 최종적으로 스타일링이 적용된 모습으로 표현
       - **추가**
         - **Node.appendChild()**
           - 한 Node를 특정 부모 Node의 자식 NodeList 중 마지막 자식으로 삽입
           - 한번에 오직 하나의 Node만 추가할 수 있다.
           - 추가된 Node 객체를 반환
           - 주어진 Node가 이미 문서에 존재하는 다른 Node를 참조한다면 현재 위치에서 새로운 위치로 이동
       - **삭제**
         - **Node.removeChild()**
           - DOM에서 자식 Node를 제거
           - 제거된 Node를 반환
       - **속성 조회**
         - **Element.getAttribute(attributeName)**	
           - 해당 요소의 지정된 값(문자열)을 반환
           - 인자(attributeName)는 값을 얻고자 하는 속성의 이름
       - **속성 설정**
         - **Element.setAttribute(name, value)**
           - 지정된 요소의 값을 설정
           - 속성이 이미 존재하면 값을 갱신, 존재하지 않으면 지정된 이름과 값으로 새 속성을 추가

    ![화면 캡처 2022-10-24 132035](C:.\화면 캡처 2022-10-24 132035.png)

    ![화면 캡처 2022-10-24 132112](C:.\화면 캡처 2022-10-24 132112.png)

    ---

## 2. Event

- ### Event object

  - 네트워크 활동이나 사용자와의 상호작용 같은 사건의 발생을 알리기 위한 객체
  - DOM 요소는 Event를 **받고** 받은 Event를 **처리할** 수 있다.
    - Event 처리는 주로 **addEventListener()**라는 **Event 처리기(Event handler)를 사용**해 다양한 html 요소를 부착하게 된다.
  - **Event 발생**
    - 마우스를 클릭하거나 키보드를 누르는 등 사용자 행동으로 발생할 수도 있고
    - 특정 메서드를 호출하여 프로그래밍적으로도 만들어 낼 수 있다.



- ### Event handler - addEventListener()

  - ![화면 캡처 2022-10-24 132738](C:.\화면 캡처 2022-10-24 132738.png)
    - EventTarget.addEventListener(type, listener[, options])
      - 지정한 Event가 대상에 전달될 때마다 호출할 함수를 설정
      - Event를 지원하는 모든 객체(Element, Document, Window 등) 를 대상(EventTarget)으로 지정 가능하다.
        - **event.target**
      - **type**
        - 반응 할 Event 유형을 나타내는 **대소문자 구분 문자열**
        - 대표 이벤트
          - input, click, submit ...
      - **listener**
        - 지정된 타입의 Event를 수신할 객체
        - JavaScript function 객체 (콜백 함수)여야 한다.
        - 콜백 함수는 발생한 Event의 데이터를 가진 Event 기반 객체를 유일한 매개변수로 받는다.



- ### Event 취소

  - **event.preventDefault()**
    - 현재 Event의 기본 동작을 중단
    - HTML 요소의 기본 동작을 작동하지 않게 막는다.
    - ex)
      - form 태그 : form 데이터 전송
      - a 태그 : 클릭 시 특정 주소로 이동



- ### lodash

  - 모듈성, 성능 및 추가 기능을 제공하는 JavaScript 유틸리티 라이브러리
  - array, object 등 자료 구조를 다룰 때 사용하는 유용하고 간편한 유틸리티 함수들을 제공한다.
  - ex)
    - reverse, sortBy, range, random ...

---

## 3. this

- ### 개념

  - 어떠한 object를 가리키는 키워드
    - (java에서의 this와 python에서의 self는 인스턴스 자기자신을 가리킨다.)
  - JavaScript의 함수는 호출될 때 this를 암묵적으로 전달 받는다.
  - 일반적인 프로그래밍 언어에서의 this와 조금 다르게 동작한다.
  - 해당 **함수 호출 방식**에 따라 this에 바인딩 되는 객체가 달라진다.
  - 즉, 함수를 선언할 때 this에 객체가 결정되는 것이 아니고, 함수를 호출할 때 **함수가 어떻게 호출 되었는지에 따라 동적으로 결정**된다.



- ### this INDEX

  1. **전역 문맥에서의 this**

     - 브라우저의 전역 객체인 window를 가리킨다.
       - **전역객체는 모든 객체의 유일한 최상위 객체를 의미한다.**
       - ![화면 캡처 2022-10-24 134156](C:.\화면 캡처 2022-10-24 134156.png)

  2. **함수 문맥에서의 this**

     - **단순 호출**
       - 전역 객체를 가리킨다.
       - 전역은 브라우저에서의 window, Node.js는 global을 의미한다.
       - ![화면 캡처 2022-10-24 134228](C:.\화면 캡처 2022-10-24 134228.png)

     

     - **Method (객체의 메서드로서)**
       - 메서드로 선언하고 호출한다면, 객체의 메서드이므로 해당 객체가 바인딩
       - ![화면 캡처 2022-10-24 134305](C:.\화면 캡처 2022-10-24 134305.png)

     

     - **Nested (Function 키워드)** 
       - forEach의 콜백 함수에서의 this가 메서드의 객체를 가리키지 못하고 전역 객체 window를 가리킨다.
       - 단순 호출 방식으로 사용되었기 때문이다.
       - **이것을 해결하기 위한 함수 표현식이 화살표 함수**
         - **화살표 함수**
           - 화살표 함수는 호출의 위치와 상관없이 상위 스코프를 사리킨다. (Lexical scope this)
           - **Lexical scope**
             - 함수를 어디서 호출하는지가 아니라 **어디에 선언**하였는지에 따라 결정된다.
             - Static scope 라고도 불리며 대부분의 프로그래밍 언어에서 따르는 방식이다.
           - **함수 내의 함수 상황에서 화살표 함수를 쓰는 것을 권장한다.**
       - ![화면 캡처 2022-10-24 134431](C:.\화면 캡처 2022-10-24 134431.png)
       - ![화면 캡처 2022-10-24 134612](C:.\화면 캡처 2022-10-24 134612.png)
       - 일반 function 키워드와 달리 메서드의 객체를 잘 가리킨다.
       - 화살표 함수에서 this는 자신을 감싼 정적 범위
       - 자동으로 한 단계 상위의  scope의 context를 바인딩한다.



- ### this와 addEventListener의 차이

  - addEventListener에서의 콜백 함수는 특별하게 function 키워드의 경우 addEventListener를 호출한 대상을 뜻한다.
  - 반면 화살표 함수의 경우 상위 스코프를 지칭하기 때문에 window 객체가 바인딩 된다.
  - 따라서, 'addEventListener'의 콜백 함수는 function 키워드를 사용하자.
  - ![화면 캡처 2022-10-24 135052](C:.\화면 캡처 2022-10-24 135052.png)