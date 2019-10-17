from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_GET, require_POST
from django.contrib.auth.decorators import login_required  # 회원인 사람만 사용할 수 있게 

from .models import Posting, Comment
from .forms import PostingModelForm, CommentModelForm



@require_GET
def posting_list(request):
    # nickname = request.COOKIE.get('nickname')  # 쿠키 꺼내오는 방법 

    postings = Posting.objects.all()
    
    return render(request, 'sns/posting_list.html', {
        'postings': postings,
        
    })


# 데코레이터 순서에 따라 튕겨져 나가는 순서도 달라진다. 
@login_required  # 로그인 된 사람만 이용할 수 있게 하는 데코레이터 
# 무조건 login 으로 하드코딩 되어있어서 우리가 views. 에 login 함수로 굳이 설정한 것 / accounts 에 설정되어 있는 데로 맞춰서 짠것 
# login 이 안되면 => 무조건 /accounts/login/ 으로 가라고 하드코딩 되어있다. 
@require_GET
def posting_detail(request, posting_id):
    posting = get_object_or_404(Posting, id=posting_id)
    comments = posting.comments.all()  # posting.comment_set 이 아닌 이유는 Model => related_name
    return render(request, 'sns/posting_detail.html', {
        'posting': posting, 
        'comments': comments,
    })


@login_required 
@require_POST
def create_posting(request):
    form = PostingModelForm(request.POST, request.FILES) # 검증 & 저장 
    if form.is_valid(): # 검증

        posting = form.save(commit=False)  # user_id 를 가져올려면 request.POST 에는 user name 을 적지 않기 때문에 
        posting.user = request.user  
        posting.save()  # 저장 => Posting 객체 return
        return redirect(posting)  # 성공하면 detail 
    else:
        return redirect('sns:posting_list')  # 실패하면 list page 

 
    # posting = Posting()
    # posting.content = request.POST.get('content')
    # posting.icon = ''
    # posting.image = request.FILES.get('image')  # 파일 받아오는 방법 
    # posting.save()

    # return redirect(posting)  # 하드 코딩하면, redirect('sns:posting_detail', posting.id)


@login_required 
@require_POST
def delete_posting(request, posting_id):
    posting = get_object_or_404(Posting, id=posting_id)
    if request.user == posting.user:  # 게시글 작성자면 삭제할 수 있게 
        posting.delete()

    return redirect('sns:posting_list')


@login_required 
@require_POST
def create_comment(request, posting_id):
    posting = get_object_or_404(Posting, id=posting_id)
    form = CommentModelForm(request.POST)  # content 만 값을 확인
    if form.is_valid():  # content 만 값을 검증 
        comment = form.save(commit=False)  # 아직 posting_id 가 비어있기 떄문에, 저장하는 것 만 / 비어있는 comment 객체를 return 해준다. 
        comment.posting = posting # comment.posting_id = posting.id  # 똑같은 코드이다... 
        comment.user = request.user  # user_id 를 가져온다. 
        comment.save()
    return redirect(posting)


@login_required 
@require_POST
def delete_comment(request, posting_id, comment_id):
    posting = get_object_or_404(Posting, id=posting_id)
    comment = get_object_or_404(Comment, id=comment_id)
    comment.delete()
    return redirect(posting)