## **그리드 시스템 / 반응형 웹**

---

## 1. CSS Layout

- **Display**
- **Position**
- **Float**

>- CSS 원칙 1 : Normal Flow (모든 요소는 네모, 위에서 아래로 왼쪽에서 오른쪽으로 쌓인다.)
>- 박스를 왼쪽, 오른쪽으로 이동시켜 **텍스트를 포함한 인라인 요소들이 주변을 감싸도록** 한다.
>- **요소가 Normal flow를 벗어나도록 한다.**
>- **속성**
>  - **none** : 기본 값
>  - **left** : 요소를 왼쪽으로 띄움
>  - **right** : 요소를 오른쪽으로 띄움
>- .clearfix::after {} : 옛날에 사용한 초기화 방식



- **Flexbox**

>- 행과 열 형태로 아이템들을 배치하는 1 차원 레이아웃 모델
>- 블록 요소를 인라인 요소로 만듦.
>
>- **축**
>   - main axis (메인 축)
>   - cross axis (교차 축, 메인 축과 수직인 축)
>- **구성 요소**
>   - Flex container (부모 요소) : **부모 요소(container)에 flex를 적용 시켜야 한다.**
>   - Flex item (자식 요소) 
>  - **inline-flex** : 테두리가 요소만큼 줄어든다.
>- **Flexbox 축**
>   - flex-direction : row (x축), 기본 값
>   - flex-direction : row-reverse (-x축)
>   - flex-direction : column (-y축)
>   - flex-direction : column-reverse (y축)
>  - **reverse를 사용하면 start와 end의 순서도 뒤집힌다.**
>- **Flex 속성**
>  - **배치 속성**
>    - **flex-direction** :
>      -  main axis 기준 방향 설정
>      - 역방향의 경우 HTML **태그 선언 순서와 시각적으로 다르니 유의**해야 한다. (웹 접근성에 영향을 미친다.)
>    - **flex-wrap**
>      - 아이템이 컨테이너를 벗어나는 경우 해당 영역 내에 배치되도록 설정
>      - 기본적으로 컨테이너 영역을 벗어나지 않도록 한다.
>      - **nowrap** : 요소를 줄여서 배치        **wrap** : 줄을 바꿔서 요소의 크기에 영향을 미치지 않는다.
>      - **flex-flow**
>        - flex-direction 과 flex-wrap 의 shorthand
>        - 설정 값을 차례로 작성
>        - ex) flex-flow:row nowrap;
>
>- **공간 나누기** : 남은 공간을 활용해 요소를 나눈다.
>  - **justify-content** (main axis)
>    - flex-start : 아이템들을 axis 시작 점으로
>    - flex-end :  아이템들을 axis 끝 쪽으로
>    - center :  아이템들을 axis 중앙으로
>    - space-between : 아이템 사이의 간격을 균일하게 분배
>    - space-around : 아이템을 둘러싼 영역을 균일하게 분배 (가질 수 있는 영역을 반으로 나눠서 양쪽에)
>    - space-evenly : 전체 영역에서 아이템 간 간격을 균일하게 분배
>    - baseline : 글자 선을 맞춰서 정렬
>  - **align-content** (cross axis)
>    - cross axis를 기준으로 공간 배분 (아이템이 한 줄로 배치되는 경우 확인할 수 없다.)
>- **정렬**
>  - **align-items** (모든 아이템을 cross axis 기준으로)
>    - stretch : 아이템들을 늘려서 맞춤
>    - flex-start
>    - flex-end
>    - center
>    - baseline
>  - **align-self** (개별 아이템)
>    - 개별 아이템을 cross axis 기준으로 정렬
>- **flex-grow** : 남은 영역을 아이템에 분배
>- **order** : 배치 순서



- **Grid**
- **기타**

----

## 2. bootstrap

- **CDN**(content Delivery Network) : 콘텐츠 (CSS, JS, Image, Text 등)을 효율적으로 전달하기 위해 여러 노드에 가진 네트워크에 데이터를 제공하는 시스템 
  - link는 head끝나는 부분 바로 위, script는 body의 끝 부분 바로 위에 넣는다.



- **spacing** (Margin and padding)

>- ```css
>  {property}{sides}-{size}
>         ->  mt-3   #(margin-top-3)  
>   <dic class="mt-3 ms-5">bootstrap-spacing</div>
>  ```
>
>- **property**
>
>  - m - margin
>  - p - padding
>
>- **sides**
>
>  - t - top
>  - b - bottom
>  - s - start(left, right)
>  - e - end(left,right)
>  - x - *-left, *-right set
>  - y - *-top, *-bottom set
>  - blank
>
>- **size**
>
>  - 1 : 0.25 rem (4px) (1rem = 16px)
>  - auto : 자동으로 채운다. (ex. mx-auto : 좌우 수평 정렬)
>  - 1 씩 증가할 때 마다 rem이 2 배씩 커진다.
>
>



- **color**

>- bootstrap 홈페이지에서 찾아서 사용한다.

- **text**

> - bootstrap 홈페이지에서 찾아서 사용한다.

- **position**

> - absolute : 부모가 static이 아니어야 한다.
> - 아니면 브라우저 기준으로 이동한다.

- **component**

>- bootstrap 홈페이지에서 찾아서 사용한다.
>- **navbar**
>- **form**
>- **button**
>- **carousel**
>  - 사진이 넘어가는 UI
>- **modal**
>  - 페이지를 이동하면 자연스럽게 사라진다.
>  - 중첩해서 넣으면 안되고 탑 레벨에 넣어야 한다.

- grid system

> 1. 12 개의 column
> 2. 6 개의 grid breakpoints가 있다.
> 3. gutter : column과 column 사이의 공간
>
> - breakpoints







---

## 3. Responsive web



