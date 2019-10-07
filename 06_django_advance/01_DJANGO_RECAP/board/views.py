from django.shortcuts import render, redirect
from .models import Article


def index(request):
    return render(request, 'board/index.html')

def list(request):
    articles = Article.objects.all()  
    # 다 가져와주세요 / [<A1>, <A2>,  ...] 객체가 여러개 리스트 비슷하게 return 이 된다.(변수명을 복수로 짓는 이유)
    # context = {'articles': articles} 하고 context
    return render(request, 'board/list.html', {
        'articles': articles,
    })

def detail(request, id):
    article = Article.objects.get(id=id) # <A_id> 
    return render(request, 'board/detail.html', {
        'article': article, 
    })
  
def new(request):
    return render(request, 'board/new.html')

def create(request):
    article = Article()
    article.title = request.POST.get('title') # db 에 저장을 하는 과정 
    article.content = request.POST.get('content')
    article.save()
    return redirect('board:detail', article.id) # redirect 절로 가~