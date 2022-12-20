from django.shortcuts import render, redirect
from .forms import ArticleForm
from .models import Articles
from django.views.decorators.http import require_safe, require_http_methods, require_POST
from django.contrib.auth.decorators import login_required
# Create your views here.

@require_safe
def index(request):
    articles = Articles.objects.all()
    context = {
        'articles':articles,
    }
    return render(request,'articles/index.html',context)

@login_required
@require_http_methods(['POST','GET'])
def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('articles:index')
    else:
        form = ArticleForm()
    context = {
        'form' : form
    }
    return render(request,'articles/create.html',context)


@require_safe
def detail(request,pk):
    article = Articles.objects.get(pk=pk)
    context = {
        'article':article,
    }
    return render(request,'articles/detail.html',context)


@require_POST
def delete(request,pk):
    if request.user.is_authenticated:
        article = Articles.objects.get(pk=pk)
        article.delete()
        return redirect('articles:index')

@login_required
@require_http_methods(['POST','GET'])
def update(request,pk):
    article = Articles.objects.get(pk=pk)
    if request.method == "POST":
        form = ArticleForm(request.POST,instance=article)
        if form.is_valid():
            form.save()
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm(instance=article)
    context = {
        'form':form,
        'article':article
    }
    return render(request,'articles/update.html',context)