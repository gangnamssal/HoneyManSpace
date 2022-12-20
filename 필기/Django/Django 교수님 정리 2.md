- 가상환경 설정하기

  1. 가상환경 만들기
     1. python -m venv {가상환경이름}(일반적으로 venv)
  2. 가상환경 실행하기
     1. 가상환경을 만들면 가상환경이름 폴더가 하나 만들어지는데 하위 경로에 activate를 실행하면 가상환경이 실행된다(Terminal이 종료되면 가상환경도 종료됨)
     2. source venv/Scripts/activate
     3. 터미널에 가상환경이름이 보이면 가상환경이 제대로 실행된 것
  3. 가상환경에 package 설정하기
     1. 가상환경을 처음만들면 아무것도 설치되지 않은 상태이다.
     2. 가상환경에 package를 설치해야 하는데, requirements.txt에 설치 목록이 있으니 참조하여 설치한다.
     3. pip install -r requirements.txt

- Django CRUD 작성하기

  1. Model 만들기 Django 에서 Model은 단순하게 데이터만 저장하는 역할을 하는게 아니라, DB에 저장하거나 읽어오는 기능도 같이 수행한다.

     1. 각 Application에서 처리할 data를 Model의 field로 정의. 기본적으로 기능을 포함하고 있기 때문에, django에서 제공하는 Model을 상속받아 작성한다.

        ```
        class Article(models.Model): 
        title = models.CharField(max_length= 10)
        content = models.TextField()
        def __str__(self): 
        	return self.title`
        ```

        

     2. Model을 생성 했다면, Model의 내용을 DB에 적용하기 위해서 migration을 수행한다.

        1. python manage.py makemigrations
        2. python manage.py migrate

     3. Model Instance를 만들어서 DB에 데이터를 넣는 방법 - 문서 확인

         

        [QuerySet API reference | Django documentation | Django](https://docs.djangoproject.com/en/3.2/ref/models/querysets/)

     4. CRUD 처리를 위한 articles.urls.py 작성하기

     ```
     path('new/',views.new,name='new'),  # 새 글 작성 화면 보여줘   path('create/',views.create,name='create'),  # 새 글 작성 저장 해줘   path('<int:pk>/detail/',views.detail, name='detail'),  # 상세 화면 보기   path('<int:pk>/edit/',views.edit, name='edit'),  # 수정 화면 보여줘   path('<int:pk>/update/',views.update, name='update'),  # 수정 해줘   path('<int:pk>/delete/',views.delete, name='delete'),  # 수정 해줘`
     ```

- Admin Site 활용하기

  1. 관리자 계정생성
     1. python manage.py createsuperuser
  2. 각 application/admin.py에 Model 추가하기
     1. admin.site.register(Article)