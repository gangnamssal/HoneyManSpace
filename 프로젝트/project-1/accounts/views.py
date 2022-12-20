from django.shortcuts import render,redirect
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm
from django.contrib.auth import login as custom_login
from django.contrib.auth import logout as custom_logout
from django.contrib.auth import update_session_auth_hash
from django.views.decorators.http import require_POST, require_http_methods, require_safe
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model

from .forms import CustomUserChangeForm, CustomUserCreationForm

# 로그인
@require_http_methods(['GET','POST'])
def login(request):
    if request.method == "POST":
        form = AuthenticationForm(request,request.POST)
        if form.is_valid():
            custom_login(request,form.get_user())
            return redirect('movies:index')
    else:
        form = AuthenticationForm()
    context = {
        'form':form,
    }
    return render(request,'accounts/login.html',context)

# 로그아웃
@login_required
def logout(request):
    if request.user.is_authenticated:
        custom_logout(request)
    return redirect('movies:index')

# 회원가입
@require_http_methods(['GET','POST'])
def signup(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            custom_login(request,user)
            return redirect('movies:index')
    else:
        form = CustomUserCreationForm()
    context = {
        'form':form,
    }
    return render(request,'accounts/signup.html',context)

# 회원정보 수정
@require_http_methods(['GET','POST'])
@login_required
def update_signup(request):
    if request.method == "POST":
        form = CustomUserChangeForm(request.POST, instance = request.user)
        if form.is_valid():
            form.save()
            return redirect('movies:index')
    else:
        form = CustomUserChangeForm(instance = request.user)
    context = {
        'form':form,
    }
    return render(request,'accounts/update_signup.html',context)

# 회원탈퇴
@login_required
def delete(request):
    if request.user.is_authenticated:
        request.user.delete()
        custom_logout(request)
    return redirect('movies:index')

# 비밀번호 변경
@require_http_methods(['GET','POST'])
@login_required
def password(request):
    if request.method=="POST":
        form = PasswordChangeForm(request.user,request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request,user)
            return redirect('movies:index')
    else:
        form = PasswordChangeForm(request.user)
    context = {
        'form':form,
    }
    return render(request,'accounts/password.html',context)

# 프로필
def profile(request,username):
    user = get_user_model()
    person = user.objects.get(username=username)
    context = {
        'person':person,
    }
    return render(request,'accounts/profile.html',context)

# 팔로우
def follows(request,user_pk):
    User = get_user_model()
    person = User.objects.get(pk=user_pk)
    if person.followers.filter(username=request.user).exists():
        person.followers.remove(request.user)
    else:
        person.followers.add(request.user)
    return redirect('accounts:profile',person.username)