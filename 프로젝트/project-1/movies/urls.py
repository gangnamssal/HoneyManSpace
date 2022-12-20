from django.conf import settings
from django.urls import path
from . import views


app_name = 'movies'
urlpatterns = [
    # 메인
    path('',views.index, name='index'),
    # 게시글 생성
    path('create/',views.create, name='create'),
    # 게시글 세부사항
    path('<int:pk>/',views.detail, name='detail'),
    # 게시글 업데이트
    path('<int:pk>/update/',views.update, name='update'),
    # 게시글 삭제
    path('<int:pk>/delete/',views.delete, name='delete'),
    # 내 게시글 보기
    path('my_article/',views.my_article,name="my_article"),
    # 댓글 생성
    path('<int:movie_pk>/comment_create/',views.comment_create, name='comment_create'),
    # 댓글 삭제
    path('<int:movie_pk>/comment_create/<int:comment_pk>/comment_delete/',views.comment_delete, name="comment_delete"),
    # 좋아요 기능
    path('<int:movie_pk>/likes/',views.likes,name='likes'),
]
