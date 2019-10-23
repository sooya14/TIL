from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_http_methods, require_GET, require_POST
from django.contrib.auth.decorators import login_required

from .forms import PostingForm, ImageForm, CommentForm
from .models import Posting, Comment, HashTag


@require_GET
def posting_detail(request, posting_id):
    posting = get_object_or_404(Posting, id=posting_id)
    # comments = posting.comments.all() => html 에서 사용할 수 있다. 
    comment_form = CommentForm()
    is_like = posting.like_users.filter(id=request.user.id).exists()

    return render(request, 'postings/posting_detail.html', {
        'posting' :posting,
        # 'comments': comments,
        'comment_form': comment_form,
        'is_like': is_like,
    })


@require_GET
def posting_list(request):
    postings = Posting.objects.all()
    return render(request, 'postings/posting_list.html', {
        'postings': postings,
    })


@login_required  
@require_http_methods(['GET', 'POST'])
def create_posting(request):
    images = request.FILES.getlist('file')

    if request.method == 'POST':
        posting_form = PostingForm(request.POST)
        # posting 이 먼저 save 되어야 positng_id 가 생기니깐 
        if posting_form.is_valid() and len(images) <= 5:
            posting = posting_form.save(commit=False)
            posting.author = request.user
            posting.save()

            # 해쉬태크 저장 부분 
            # content = posting.content 
            words = posting.content.split()
            for word in words:
                if word[0] == '#':
                    tag = HashTag.objects.get_or_create(content=word)  # get_or_create 의 return == list # 있으면 만들고 없으면 가져온다. 
                    posting.hashtags.add(tag[0])

            for image in images:
                request.FILES['file'] = image 
                image_form = ImageForm(files=request.FILES)  # Form 류는 request 로 시작하는 객체여야한 사용이 가능하다.
                if image_form.is_valid():
                    image = image_form.save(commit=False)
                    image.posting = posting  # image.posting_id = posting.id
                    image.save()
            return redirect(posting)    
    else:
        posting_form = PostingForm()
        image_form = ImageForm()

    return render(request, 'postings/posting_form.html', {
        'posting_form': posting_form,
        'image_form': image_form,
    })


@login_required
@require_http_methods(['GET', 'POST'])
def update_posting(request, posting_id):
    posting = get_object_or_404(Posting, id=posting_id)
    if posting.author == request.user:  # 아무나 수정할 수 없게 하기 위해
        if request.method == 'POST':
            form = PostingForm(request.POST, instance=posting)
            if form.is_valid():
                posting = form.save()
                return redirect(posting)
        else:
            form = PostingForm(instance=posting)

    else:
        return redirect(posting)  # 게시글 작성자랑 author 랑 같지 않으면 수정할 수 없게 list 보여준다. 
    return render(request, 'postings/posting_form.html', {
        'posting_form': form,  # {% bootstrap_form posting_form %} 이렇게 작성되어있기 때문에 / create_posting이랑 html 을 같이 사용하고 있기 때문에 
    })
    


@login_required
@require_POST
def delete_posting(request, posting_id):
    posting = get_object_or_404(Posting, id=posting_id)
    posting.delete()
    return redirect('postings:posting_list')


@login_required
@require_POST
def create_comment(request, posting_id):
    posting = get_object_or_404(Posting, id=posting_id)
    form = CommentForm(request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.author = request.user
        comment.posting = posting  # comment.posting_id = posting.id
        comment.save()
        
    return redirect(posting)  # 코멘트 생성 후 본 게시글로 갈거니깐


@login_required
@require_POST  # 좋아요를 하고 해제하는 것 모두 데이터 베이스에 한줄을 추가하고 삭제하는 기능
def toggle_like(request, posting_id):
    posting = get_object_or_404(Posting, id=posting_id)
    user = request.user

    # 좋아요를 누른 user 라면,
    if posting.like_users.filter(id=user.id).exists():  # 
        posting.like_users.remove(user)
    else:
        posting.like_users.add(user)

    return redirect(posting)