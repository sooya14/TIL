from django.shortcuts import render, redirect, get_object_or_404 
from django.views.decorators.http import require_GET, require_POST

from .models import Article


@require_GET
def index(request):
    return render(request, 'board/index.html')


@require_GET
def list(request):
    articles = Article.objects.all()  
    # 다 가져와주세요 / [<A1>, <A2>,  ...] 객체가 여러개 리스트 비슷하게 return 이 된다.(변수명을 복수로 짓는 이유)
    # context = {'articles': articles} 하고 context
    return render(request, 'board/list.html', {
        'articles': articles,
    })


@require_GET
def detail(request, id):
    article = get_object_or_404(Article, id=id) 
    # article 에서 있으면 아래로 진행하고 없으면 404 내보내겟다. /하나 잡는 행위는 무조건 필요

    return render(request, 'board/detail.html', {
        'article': article, 
    })


@require_GET
def new(request):
    return render(request, 'board/new.html')


@require_POST
def create(request):
    article = Article()
    article.title = request.POST.get('title') # db 에 저장을 하는 과정 
    article.content = request.POST.get('content')
    article.save()
    return redirect('board:detail', article.id) # redirect 절로 가~


@require_GET
def edit(request, id):
    article = get_object_or_404(Article, id=id)
    # id 하나를 찾기 위한 코드
    article = Article.objects.get(id=id)
    return render(request, 'board/edit.html', {
        'article': article,
    })


@require_POST # db 관련된 일을 할 때 POST 라고 생각해도 될듭?
def update(request, id):
    article = get_object_or_404(Article, id=id)
    article = Article.objects.get(id=id)
    article.title = request.POST.get('title')
    article.content = request.POST.get('content')
    article.save()
    return redirect('board:detail', article.id)  # 안되면 하드코딩으로 해보기 


@require_POST  # 데코레이터(이 함수에 대한 데코레이팅이 된다.) / POST 로 요청했을 때만 작동해랏! 
# 데코레이터 설정을 안했으면 직접 주소에 delete 추가해서 GET 요청을 통해서도 지워진다. 
def delete(request, id):
    article = get_object_or_404(Article, id=id)
    article = Article.objects.get(id=id)
    article.delete()
    return redirect('board:list')