from urllib.parse import urlparse
from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
    # 로그인
    path('login/',views.login, name='login'),
    # 로그아웃
    path('logout/',views.logout, name='logout'),
    # 회원 가입
    path('signup/',views.signup, name='signup'),
    # 회원 정보 수정
    path('update_signup/',views.update_signup, name='update_signup'),
    # 회원 탈퇴
    path('delete/',views.delete,name='delete'),
    # 비밀번호 변경
    path('password/',views.password,name="password"),
    # 프로필
    path('profile/<str:username>/',views.profile,name='profile'),
    # 팔로우
    path('<int:user_pk>/follows/',views.follows,name='follows'),
]
