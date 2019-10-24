from django.shortcuts import render, redirect, get_object_or_404
from .models import Article
from .forms import ArticleModelForm
from django.contrib.auth import get_user_model  ## 
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_GET, require_POST, require_http_methods


@require_GET
def article_list(request):
    articles = Article.objects.all()
    return render(request, 'articles/article_list.html', {
        'articles': articles,
    })

@login_required  ##
@require_http_methods(['GET', 'POST'])  ##
def article_create(request):
    if request.method == 'POST':
        form = ArticleModelForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)  ##
            article.user = request.user 
            article.save()
            return redirect('articles:article_detail', article.id)  ## 
            
    else:
        form = ArticleModelForm()
    return render(request, 'articles/form.html', {
        'form': form,
    })
    

@require_GET
def article_detail(request, article_id):
    article = get_object_or_404(Article, id=article_id)  ##
    return render(request, 'articles/article_detail.html', {
        'article': article,
    })


# @login_required  ##
# @require_http_methods(['GET', 'POST']) ## 
# def article_update(request, article_id):
#     article = get_object_or_404(Article, id=article_id)
#     if request.user != article.user:
#         return redirect('articles:article_list')
#     if request.method == 'POST':
#         form = ArticleModelForm(request.POST, instance=article)
#         if form.is_valid():
#             article.save()
#             return redirect('articles:article_detail', article.id)                
#     else:
#         form = ArticleModelForm(instance=article)
#     return render(request, 'articles/form.html', {
#         'form': form,
#     })

@login_required
@require_http_methods(['GET', 'POST'])  
def article_update(request, article_id):
# Create 복-붙 후 Update 추가사항
    # 0. article 하나 찾기
    article = get_object_or_404(Article, id=article_id)
    # 1. User 비교하기
    if article.user != request.user:
        return redirect('articles:article_list')

    if request.method == 'POST':
        # 2. instance= 주기
        form = ArticleModelForm(request.POST, instance=article)
        if form.is_valid():
            # 3. 고치기 (사실 안고쳐도 되긴함..)
            article = form.save()
            return redirect('articles:article_detail', article.id)
    else:
        # 4. 또 instance= 주기
        form = ArticleModelForm(instance=article)
    return render(request, 'articles/form.html', {
        'form': form,
    })




@login_required ##
@require_POST  ##
def article_delete(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    if article.user != request.user:
        return redirect('articles:article_list')
    else:
        article.delete()
        return redirect('articles:article_list')


## 아무런 데코레이터를 사용하지 않는다. 
def article_like(request, article_id):
    article = get_object_or_404(Article, id=article_id)

    ########################################
    user = request.user
    if user in article.like_users.all():
        article.like_users.remove(user)
    else:
        article.like_users.add(user)

    return redirect('articles:article_detail', article.id)
    ####################################################

 




