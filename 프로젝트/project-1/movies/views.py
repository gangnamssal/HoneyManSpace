from tkinter.tix import InputOnly
from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST,require_safe,require_http_methods
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model

import movies

from .forms import MovieForm,CommentForm
from .models import Movie,Comment

# Create your views here.

# 전체 영화 데이터 조회, GET
@ require_safe
def index(request):
    movies = Movie.objects.all()
    context = {
        'movies':movies,
    }
    return render(request,'movies/index.html',context)

# create 렌더링
# 유효성 검증 및 영화 데이터 저장 후 detail로 보내줌
# GET,POST
@require_http_methods(['GET','POST'])
@login_required
def create(request):
    if request.method == 'POST':
        form = MovieForm(request.POST)
        if form.is_valid():
            movie = form.save(commit=False)
            movie.user = request.user
            movie.save()
            return redirect('movies:detail',movie.pk)
    else:
        form = MovieForm()
    context = {
        'form':form,
    }
    return render(request,'Movies/create.html',context)

# 단일 영화 데이터 조회 및 detail로 렌더링
# GET
@require_safe
@login_required
def detail(request,pk):
    movie = Movie.objects.get(pk=pk)
    comment = CommentForm()
    comments = movie.comment_set.all()
    context = {
        'movie':movie,
        'comment':comment,
        'comments':comments,
    }
    return render(request,'movies/detail.html',context)

# 수정 대상 영화 데이터 조회 및 update 렌더링
# 유효성 검증 및 영화 데이터 수정 후 detail로 보냄
# GET, POST
@require_http_methods(['GET','POST'])
@login_required
def update(request,pk):
    movie = Movie.objects.get(pk=pk)
    if request.user == movie.user:
        if request.method=="POST":
            form = MovieForm(request.POST, instance=movie)
            if form.is_valid():
                form.save()
                return redirect('movies:detail',movie.pk)
        else:
            form = MovieForm(instance=movie)
    else:
        return redirect('movies:detail',movie.pk)
    context = {
        'form':form,
        'movie':movie,
    }
    return render(request,'movies/update.html',context)


# 단일 영화 데이터 삭제 및 index로 보냄
# POST
@login_required
def delete(request,pk):
    movie = Movie.objects.get(pk=pk)
    if request.method=="POST":
        if request.user.is_authenticated:
            if request.user == movie.user:
                movie.delete()
    return redirect('movies:index')

# 내 게시글 보기
def my_article(request):
    movies = Movie.objects.all()
    context = {
        'movies':movies,
    }
    return render(request,'movies/my_article.html',context)

# 댓글 
@require_POST
@login_required
def comment_create(request,movie_pk):
    movie = Movie.objects.get(pk=movie_pk)
    if request.method == "POST":
        comment_create = CommentForm(request.POST)
        if comment_create.is_valid():
            comment = comment_create.save(commit=False)
            comment.movie = movie
            comment.user = request.user
            comment.save()
        return redirect('movies:detail',movie_pk)

# 댓글 삭제 
@login_required
def comment_delete(request,movie_pk,comment_pk):
    comment = Comment.objects.get(pk=comment_pk)
    if request.user.is_authenticated:
        if request.user == comment.user:
            comment.delete()
    return redirect('movies:detail',movie_pk)

# 좋아요 기능
def likes(request,movie_pk):
    movie = Movie.objects.get(pk=movie_pk)
    if movie.like_users.filter(pk=request.user.pk).exists():
        movie.like_users.remove(request.user)
    else:
        movie.like_users.add(request.user)
    return redirect('movies:detail',movie.pk)
