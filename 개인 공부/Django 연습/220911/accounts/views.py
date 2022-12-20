from importlib import import_module
from multiprocessing import context
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm
from django.contrib.auth import login as custom_login
from django.contrib.auth import logout as custom_logout
from .forms import CustomUserChangeForm, CustomUserCreationForm
from django.contrib.auth import update_session_auth_hash
from django.views.decorators.http import require_safe, require_POST, require_http_methods
from django.contrib.auth.decorators import login_required
# Create your views here.

@require_http_methods(['POST','GET'])
def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request,request.POST)
        if form.is_valid():
            custom_login(request,form.get_user())
            return redirect(request.GET.get('next') or 'articles:index')
    else:
        form = AuthenticationForm()
    context = {
        'form':form
    }
    return render(request,'accounts/login.html',context)


@require_POST
def logout(request):
    if request.user.is_authenticated:
        custom_logout(request)
        return redirect('articles:index')

@require_http_methods(['POST','GET'])
def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            custom_login(request, user)
            return redirect('articles:index')
    else:
        form = CustomUserCreationForm()
    context = {
        'form':form,
    }
    return render(request,'accounts/signup.html',context)


@require_POST
def delete(request):
    if request.user.is_authenticated:
        request.user.delete()
        custom_logout(request)
        return redirect('articles:index')

@login_required
@require_http_methods(['POST','GET'])
def update(request):
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('articles:index')
    else:
        form = CustomUserChangeForm(instance=request.user)
    context = {
        'form':form
    }
    return render(request,'accounts/update',context)

@login_required
@require_http_methods(['POST','GET'])
def change_password(request):
    if request.method == "POST":
        form = PasswordChangeForm(request.user,request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request,form.user)
            return redirect('articles:index')
    else:
        form = PasswordChangeForm(request.user)
    context = {
        'form':form
    }
    return render(request,'accounts/change_password.html',context)