from django.shortcuts import render, redirect, get_object_or_404
# User 모델을 가져오는 함수 
from django.contrib.auth import get_user_model
# decorator
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_GET, require_POST, require_http_methods

from .models import Article
from .forms import ArticleForm

@require_GET
def article_list(request):
    # object's'
    articles = Article.objects.all()
    return render(request, 'articles/index.html', {
        'articles': articles,
    })


@require_GET
def article_detail(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    return render(request, 'articles/detail.html', {
        'article': article,
    })

# ★
@login_required # CRD 는 모두 @login_required
@require_http_methods(['GET', 'POST'])  # 이번 셤에서는 안써도 된다. 썼다가 틀릴것같으면 쓰지 마세요용 
def article_create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.user = request.user  # 혹은 article.user_id = request.user.id
            article.save()
            return redirect('articles:article_detail', article.id)
    else:
        form = ArticleForm()
    return render(request, 'articles/form.html', {
        'form': form,
    })

# ★
@login_required # CRD 는 모두 @login_required
@require_http_methods(['GET', 'POST'])
def article_update(request, article_id):
        # Create 복붙 후, Update 추가사항
        
    # 0. article 하나 찾기 
    article = get_object_or_404(Article, id=article_id)
    # 1. User 비교하기
    if article.user != request.user:
        return redirect('articles:article_list')
    if request.method == 'POST':
    # 2. instance 주기 
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            # 3. 지우기 (사실 안지워도 되긴함...)
            # article = form.save(commit=False)
            # article.user = request.user  # 혹은 article.user_id = request.user.id
            article.save()
            return redirect('articles:article_detail', article.id)
    else:
        # 4. 또 instance 주기 
        form = ArticleForm(instance=article)
    return render(request, 'articles/form.html', {
        'form': form,
    })



@login_required # CRD 는 모두 @login_required
@require_POST
def article_delete(request, article_id):
    # 주의! user 비교하기 
    article = get_object_or_404(Article, id=article_id)
    if request.user != article.user:
        return redirect('articles/article_list')


def like(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    user = request.user 
    # if article.like_users.filter(id=user.id).exists():
    if user in article.like_users.all():  # 이미 좋아요
        article.like_users.remove(user)  # 그니까 지움요
    else:
        article.like_users.add(user)
    return redirect('articles:article_list')
    
