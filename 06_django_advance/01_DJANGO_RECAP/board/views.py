from django.shortcuts import render, redirect, get_object_or_404 
from django.views.decorators.http import require_GET, require_POST, require_http_methods

from .forms import ArticleModelForm, CommentModelForm, ArticleForm
from IPython import embed # 왜 에러가 났는지 알수 있다. 디버깅처럼 
from .models import Article, Comment




# CRUD
@require_http_methods(['GET', 'POST'])  # GET, POST 만을 처리하겠다. (비공식적으로 많은 method 가 존재하기 때문에)
def new_article(request):
    # 요청이 GET/POST 인지 확인한다. 
    # 만약 POST 라면 
    if request.method == 'POST':
        # ArticleModelForm 의 인스턴스를 생성하고 Data 를 채운다. (binding)
        form = ArticleModelForm(request.POST)  # 데이터를 넣어서 유효한지 검증하는 용도 
        #embed()  # 나중에 지워줘야한다. 
        # binding 된 form 이 유효한지 체크한다. 
        if form.is_valid():
            # 유효하다면 form을 저장한다. 
            article = form.save()
            # 저장한 article 로 redirect 한다. 
            return redirect(article)  # redirect('board:article_detail', article.id) 인데 models.py 에 get_absolute_url 함수를 통해서 줄일 수 있다...... 
        # form 이 유효하지 않다면,
        # else:
        #     # 유효하지 않은 입력데이터를 담은 HTML과 에러메세지를 사용자한테 보여준다. 
        #     return render(request, 'board/new.html', {
        #         'form': form, 
        #     })
            
    # GET 이라면 
    else:
        # 비어있는 form 을 만든다. 
        form = ArticleModelForm()  # 비어 있는 html 만들어준다
        # form 과 html 을 사용자에게 보여준다. 
    return render(request, 'board/new.html', {
        'form': form,
    })

def article_list(request):
    articles = Article.objects.all()
    return render(request, 'board/list.html', {
        'articles': articles,
    })

@require_GET
def article_detail(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    comments = article.comment_set.all()  # 모든 comments 를 리스트로 저장한다. # Comment.objects.filter(article_id=article.id)
    # article views 라고 해서 comments 를 안에 설정하는 것을 어색해 하지말고,
    comment_form = CommentModelForm()  # 화면을 그냥 볼때는 () 비워 놓고,

    return render(request, 'board/detail.html', {
        'article': article,
        'comments': comments,
        'comment_form': comment_form,
    })

@require_http_methods(['GET', 'POST'])
def edit_article(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    if request.method == 'POST':
        form = ArticleModelForm(request.POST, instance=article)  # 데이터 넘어온 것을 받는 부분 
        if form.is_valid():
            article = form.save()
            return redirect(article)

    else:  # GET 부분 : 종이주세요~
        form = ArticleModelForm(instance=article)  # 찾은 그 객체를 인자에 여기에 넣을 것이다! / 있던 것을 찾아서 넣는 부분 
    return render(request, 'board/edit.html', {
        'form': form,
    })


@require_POST  # 삭제는 데이터베이스에 영향을 주기 때문
def delete_article(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    article.delete()
    return redirect('board:article_list')


@require_POST
def new_comment(request, article_id):  # /board/articles/N/comments/new
    article = get_object_or_404(Article, id=article_id)

    # comment = Comment()
    # comment.content = request.POST.get('comment_content')
    # comment.article_id = article.id  # 몇번 게시글의 댓글인지를 알기 위해서 url 에 N 이 있다. 
    # comment.save()

    form = CommentModelForm(request.POST)  # 화면을 보여주는 것이 아니라 저장을 담당하는 부분(POST) => 날라온 데이터를 받아줘야한다. 
    # 판별하고 싶을 때는 request.POST 를 채워넣어야한다. 
    # embed()
    if form.is_valid():  # id 는 신경을 쓰지 않는다. 
        # comment = Comment()
        # comment.content = request.POST.get('content')
        comment = form.save(commit=False)  # comment = form.save() 는 의미가 없다. comment의 detail 화면으로 갈 필요가 없기 때문에 # commit : 저장하는 척
        # id 는 사용자가 직접 입력하지 않기 때문에 commit 사용 
        # 저장은 중요하니까..? 제어를 뻇어 와서 검증할라고 
        comment.article_id = article.id  # 몇번 게시글의 댓글인지를 알기 위해서 url 에 N 이 있다. 
        comment.save()
        
    # 유효하지 않아도 detail 화면으로 간다. 그래서 이걸로 끝!
    return redirect(article)


@require_POST  # 데이터를 삭제하니까 POST
def delete_comment(request, article_id, comment_id):
    # article = get_object_or_404(Article, id=article_id)
    # comment = get_object_or_404(Comment, id=comment_id)
    # if comment in article.comment_set.all():  # 게시글에 달린 댓글의 모든 것 
    #     comment.delete()
    # return redirect(article)

    # 가성비 코드 
    comment = get_object_or_404(Comment, id=comment_id)
    comment.delete()  # db 에서 삭제되고, 
    return redirect(comment.article)  # 이 함수가 끝난 후에 메모리에서 삭제된다. => 메모리삭제와 db삭제는 다르다. 

    




# # (참고사항) Create Article with Form 
# def new_article_with_form(request):
#     if request.method == 'POST':
#         form = ArticleForm(request.POST)

#         if form.is_valid():           
#             article = ArticleForm()
#             # article.title = request.POST.get('title') # 검증되지 않은 데이터 / 오염된 데이터가 들어갈 수 있기 때문에 가급적이면 사용하지 않는 것이 좋다. 
#             article.title = form.cleaned_data.get('title') # 검증된 데이터 / 데이터가 자동으로 들어가지 않아서 직접 하나씩 꼽아줘야한다. 
#             article.content = form.cleaned_data.get('content')
#             article.save()
#             return redirect(article)

#     else:
#         form = ArticleForm()

#     return render(request, 'board/new.html', {
#         'form': form,
#     })




###############################################################################################
# from .models import Article
# from .forms import ArticleModelForm

# @require_GET
# def index(request):
#     return render(request, 'board/index.html')


# @require_GET
# def list(request):
#     articles = Article.objects.all()  
#     # 다 가져와주세요 / [<A1>, <A2>,  ...] 객체가 여러개 리스트 비슷하게 return 이 된다.(변수명을 복수로 짓는 이유)
#     # context = {'articles': articles} 하고 context
#     return render(request, 'board/list.html', {
#         'articles': articles,
#     })


# @require_GET
# def detail(request, id):
#     article = get_object_or_404(Article, id=id) 
#     # article 에서 있으면 아래로 진행하고 없으면 404 내보내겟다. /하나 잡는 행위는 무조건 필요

#     return render(request, 'board/detail.html', {
#         'article': article, 
#     })


# # ArticleModelForm 함수 설정했을 때
# def new(request):
#     if request.method == 'POST':
#         form = ArticleModelForm(request.POST)  # 알아서 데이터 분류 작업을 해준다. 

#         if form.is_valid():  # title 이 2글자 보다 길면 저장하라 
#             article = form.save()
#             return redirect(article) 
#     else:  # GET 요청일 때 
#         form = ArticleModelForm()  

#     return render(request, 'board/new.html', {
#         'form': form,
#     })


# # def new(request):
# #     if request.method == 'POST':
# #         article = Article()
# #         article.title = request.POST.get('title') 
# #         article.content = request.POST.get('content')
# #         article.save()
# #         # return redirect('board:detail', article.id)
# #         return redirect(article) # get_absolute_url 함수 사용하면 이렇게 간단하게 코드 가능
        
# #     else:  # GET 면 저장을 한다. 
# #         return render(request, 'board/new.html')



# # @require_POST
# # def create(request):
# #     article = Article()
# #     article.title = request.POST.get('title') # db 에 저장을 하는 과정 
# #     article.content = request.POST.get('content')
# #     article.save()
# #     return redirect('board:detail', article.id) # redirect 절로 가~ / detail url 로 가랏


# # @require_GET
# def edit(request, id):
#     article = get_object_or_404(Article, id=id)
#     if request.method == 'POST':
#         article.title = request.POST.get('title')
#         article.content = request.POST.get('content')
#         article.save()
#         # return redirect('board:detail', article.id)
#         return redirect(article)

#     else:
#         # id 하나를 찾기 위한 코드
#         return render(request, 'board/edit.html', {
#             'article': article,
#         })
        


# # @require_POST # db 관련된 일을 할 때 POST 라고 생각해도 될듭?
# # def update(request, id):
# #     article = get_object_or_404(Article, id=id)
# #     article = Article.objects.get(id=id)
# #     article.title = request.POST.get('title')
# #     article.content = request.POST.get('content')
# #     article.save()
# #     return redirect('board:detail', article.id)  # 안되면 하드코딩으로 해보기 


# @require_POST  # 데코레이터(이 함수에 대한 데코레이팅이 된다.) / POST 로 요청했을 때만 작동해랏! 
# # 데코레이터 설정을 안했으면 직접 주소에 delete 추가해서 GET 요청을 통해서도 지워진다. 
# def delete(request, id):
#     article = get_object_or_404(Article, id=id)
#     article = Article.objects.get(id=id)
#     article.delete()
#     return redirect('board:list')