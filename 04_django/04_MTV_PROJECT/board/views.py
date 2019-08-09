from django.shortcuts import render, redirect
from .models import Article  # views.py 와 models.py 연결


# Create
def new(request):  # 새로운 게시글을 작성할 화면 
        return render(request, 'board/new.html')


def create(request):  # 입력 데이터를 DB 에 저장 
    # requst.GET => {'input_title: 제목제목, 'input_content': 내용내용}
    article = Article()
    article.title = request.GET.get('input_title')
    article.content = request.GET.get('input_content')
    article.save()
    return redirect(f'/board/articles/{article.id}') 


# Read
def index(request):  # 도든 게시글 목록을 보여주는 view
    articles = Article.objects.all()  # [] => 리스트니깐 여러개가 튀어나온다. 
    return render(request, 'board/index.html', {
        'articles': articles,
    })


def show(request, article_id):  # 특정 게시글을 보여주는 view
    article = Article.objects.get(id=article_id)  # 하나만 튀어나온다. 
    return render(request, 'board/show.html', {
        'article': article
    })

# Update
def edit(request):  # 특정 게시글을 수정할 화면 
    return render(request, 'board/edit.html')


# Delete 
def delete(request, article_id):  # 특정 게시글을 삭제하는 view(일)
    article = Article.objects.get(id=article_id)
    article.delete()
    return redirect('/board/articles/')
