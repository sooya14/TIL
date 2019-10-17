from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_GET, require_POST, require_http_methods  ##

from .models import Article, Comment
from .forms import ArticleModelForm, CommentModelForm ##


def article_list(request):
    articles = Article.objects.all() ##
    return render(request, 'article/article_list.html', {
        'articles': articles,
    })


@require_GET
def article_detail(request, article_id):
    article = get_object_or_404(Article, id=article_id)

    return render(request, 'article/article_detail.html', {  ##
        'article': article,
    })


##
@require_http_methods(['GET', 'POST'])
def new_article(request):
    if request.method == 'POST':
        form = ArticleModelForm(request.POST)
        if form.is_valid():
            article = form.save()
            return redirect(article)

    else:
        form = ArticleModelForm()
    return render(request, 'article/new_article.html', {
        'form': form,
    })

