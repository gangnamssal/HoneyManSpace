# **git 설치, typora 설치**



## - **python  문법**

1. ### **저장**

   * dict = {key:value, key:value, ...}

   ​        ex) phone_book.get('일식') ->  none

   * list : print(f'오늘의 메뉴는 {seleced} 입니다.')

   

2. ### **조건문(분기문)**

   * is_~~ = True or False : 플래그

   * if, else =  if 조건문: (단독사용 o)

   ​                                조건문이 참 일때 실행하는 문장

   ​                        elif 조건문: (단독사용 x)

   ​                                 조건문이 참 일때 실행

   ​                        else:(조건 x)

   ​                                조건문이 거짓일 때 실행하는 문장

   ​                         --> 조건들이 상호 베타적이여야 한다. 

   

3. ### **반복**

   * for : 덩어리 데이터를 하나씩 접근 하도록 해줌

   ​        ex) for  데이터 하나 in 데이터 덩어리:

   ​             for element in menu:

   ​                    print(element)

   * for 문을 활용한 list index접근

     -range( start,stop,step)  사용 : start는 포함 stop은 미포함

     ex) for i in range(10)

   * while   

     

4. ### **함수**

   -코드 덩어리

   

5. ### **API받기**

   **1)**pip install requests
   
   **2)**
   
   ​      **ex1**)  \# requests : http 요청을 생성한다.
   
   ​                   url = "http://www.naver.com"
   
   ​                   requests.get(url)
   
   ​                   response = requests.get(url)
   
   ​                   print(response.text)
   
   ​      
   
   ​       **ex2**) import requests
   
   ​               \# requests : http 요청을 생성한다.
   
   ​                   url = "https://api.agify.io/?name=symon"
   
   ​                   response = requests.get(url).json()
   
   ​                   name = response.get('name')
   
   ​                   age = response.get('age')
   
   ​                   count = response.get('count')
   
   ​                   print(f'이름 : {name} 나이 : {age} 카운터 : {count}')
   
   
   
   **3)** json : 자바 스크립트 오브젝트 노테이션
   
   - [{"key":"value"}]의 형태 혹은  {"key":"[   ]"}
   
   - 위의 문자열을 파이썬 객체로 바꾸는 과정을 parsing이라고 한다.
   
     
   
     **4) API요청**

- 요청 파라미터 : 클라이언트에서 서버로 보내는 데이터

- 요청 파라미터를 추가하는 방법 :  get 요청시 -> 방법 :  URL?파라미터이름 = 파라미터값&파라미터이름= 파라미터값&파라미터이름...

- url:   http://apis.data.go.kr/B552584/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty  

- serviceKey=SQiaAlwdoc70572tiUs%2FobUAI8F82Xq3oKYo8Rc39gcINPh42MTNV9IpuXgT%2FiJC1QFsT3kRfCdnBABYmQzgiQ%3D%3D

- sidoName=대구

- 요청 파라미터 :   http://apis.data.go.kr/B552584/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty?serviceKey=SQiaAlwdoc70572tiUs%2FobUAI8F82Xq3oKYo8Rc39gcINPh42MTNV9IpuXgT%2FiJC1QFsT3kRfCdnBABYmQzgiQ%3D%3D&sidoName=대구&returnType=json



**ex)**

import requests

\# 텍스트정보 불러오기

url = "http://apis.data.go.kr/B552584/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty?serviceKey=SQiaAlwdoc70572tiUs%2FobUAI8F82Xq3oKYo8Rc39gcINPh42MTNV9IpuXgT%2FiJC1QFsT3kRfCdnBABYmQzgiQ%3D%3D&sidoName=대구&returnType=json"

response = requests.get(url).json()

\# print(response)

\# statiion : 대명동

result = response.get('response')

body = result.get('body')

items = body.get('items')

print(type(items))



dust = -1

a = 0

sum = 0

for item in items:

  \# item >>> 하나하나가 dictionary : 동정보와 미세먼지 정보를 포함

  \# 하나하나 확인하면서, 대명동만 꺼낼 것.

  \# item이 가지고 있는 stationName 속성을 확인하고, 대명동이라면

  \# 저장하기

\#   if item.get('stationName') == '대명동':

\#     # 미세먼지 농도 가져오기

\#     dust = item.get('pm10Value')

\# print(f'대명동의 현재 미세먼지 농도는 {dust} 입니다.')

​    dust = item.get('pm10Value')

​    sum += int(dust)

a = sum / len(items)

print(f'대구의 현재 평균 미세먼지 농도는 {a} 입니다.')



## - git 사용법

### 1. 기본 문법

> mkdir ~~ : 새 폴더를 만드는 명령어

> ls : 현재 작업 중인 디렉토리의 폴더/파일 목록을 보여주는 명령어

> cd ~~ : 현재 작업중인 디렉토리를 변경하는 명령어

> > cd ~ : 홈으로 이동

> touch ~~.txt : 파일을 생성하는 명령어

> rm : 파일을 삭제하는 명령어

> > -r 옵션을 주면 폴더 삭제 가능



### 2. 기본 용어

> repository : 특정 디렉토리를 버전 햣 관리하는 저장소
>
> 편집기 : vim - i 입력 (나갈 때 esc or :q!)
>
> README.md : 깃을 생성하면 만들어지는 파일
>
> IGNORE.md : touch .gitignore로 생성
>
> > 구글에 git ignore 검색
> >
> > 복사 붙여넣고
> >
> > git add .
> >
> > git commit -m
>
> >  **git init** 명령어로 로컬 저장소를 생성
> >
> > .git 디렉토리에 버전 관리에 필요한 모든 것이 들어있음
>
> 1. 깃 repository 생성 (git init)(숨긴파일 켜기)
>
> 2. git add .을 입력하면 지금부터 모든 파일을 깃에서 관리하겠다는 의미.(git status : 깃의 상태 확인) 
>
> 3. git commit -m"" : (-m : 바꾼 것의 요약) 
>
> 4. git config --global user.name " "
>
> 5. git config --global user.email " "
>
> 6. 다시 git commit -m"" : (-m : 바꾼 것의 요약)를 친다.
>
> 7. git log : 커밋한 히스토리를 볼 수 있다.(HEAD : 지금 내가 작업하고 있는 공간)
>
>    > master(main branch) : 메인 가지
>    >
>    > branch : 메인에서 여러 응용을 하여 많은 가지들이 생긴 것
>    >
>    > master branch : master와 branch가 합쳐진 상태
>
> 8. git restore . : 저장
>
> 
>
> ### branch
>
> 1. git branch 이름 : 브랜치 생성
> 2. git branch : 브랜치 확인
> 3. git  switch 브랜치 이름 : (브랜치로 이동)
>
> > branch의 변경 사항은 master에 저장해야 한다.(step forward)
> >
> > 1. git merge 브랜치 이름 : 마스터에 브랜치의 내용을 합친다.
> >
> >    > 충돌 : 마스터가 브랜치보다 앞에 있는데 병합할려고 할 때
> >    >
> >    > 수정할 것을 수정하고 다시 저장후 커밋
> >
> > 2. git branch -d 브랜치 이름 : b1을 없앤다.



## 3. git lab 

1. git clone 깃랩에서 클론 주소(https) .  : .이 없으면 새로운 폴더가 생성되고 안에 깃 폴더가 생성됨.
2. 로그인
3. git remote -v : 현재 깃이랑 연결된 repository를 보여줌.
4. git push origin master : master에 업로드
5. git pull origin master : master에 다운로드

## - markdown(마크다운)

- https://gist.github.com/ihoneymon/652be052a0727ad59601 설명 나와있음.

- 택스트 기반의 가벼운 마크업 언어

- 문서의 구조와 내용을 같이 쉽고 빠르게 적고자 탄생

- 소스코드 이쁘게 보내기 : `이거 3개 쓰고 python적기.

- ctrl + / : 소스코드모드 읽기 모드 바꾸기

- shift + tap : 내여쓰기

- tap : 들여쓰기

- 상대경로 : 현재 문서를 기준으로 경로를 알려줌.(../를 사용)

  (꿀팁 : 윈도우 + shift + s 화면캡쳐)