from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_GET, require_POST

from .models import Posting, Comment
from .forms import PostingModelForm, CommentModelForm

# Create your views here.
def posting_list(request):
    postings = Posting.objects.all()
    
    return render(request, 'sns/posting_list.html', {
        'postings': postings,
    })

@require_GET
def posting_detail(request, posting_id):
    posting = get_object_or_404(Posting, id=posting_id)
    comments = posting.comments.all()  # posting.comment_set 이 아닌 이유는 Model => related_name
    return render(request, 'sns/posting_detail.html', {
        'posting': posting, 
        'comments': comments,
    })

@require_POST
def create_posting(request):
    form = PostingModelForm(request.POST, request.FILES) # 검증 & 저장
    if form.is_valid(): # 검증
        posting = form.save()  # 저장 => Posting 객체 return
        return redirect(posting)  # 성공하면 detail 
    else:
        return redirect('sns:posting_list')  # 실패하면 list page 

 
    # posting = Posting()
    # posting.content = request.POST.get('content')
    # posting.icon = ''
    # posting.image = request.FILES.get('image')  # 파일 받아오는 방법 
    # posting.save()

    # return redirect(posting)  # 하드 코딩하면, redirect('sns:posting_detail', posting.id)


@require_POST
def delete_posting(request, posting_id):
    posting = get_object_or_404(Posting, id=posting_id)
    posting.delete()

    return redirect('sns:posting_list')

@require_POST
def create_comment(request, posting_id):
    posting = get_object_or_404(Posting, id=posting_id)
    form = CommentModelForm(request.POST)  # content 만 값을 확인
    if form.is_valid():  # content 만 값을 검증 
        comment = form.save(commit=False)  # 아직 posting_id 가 비어있기 떄문에, 저장하는 것 만 / 비어있는 comment 객체를 return 해준다. 
        comment.posting = posting # comment.posting_id = posting.id  # 똑같은 코드이다... 
        comment.save()
    return redirect(posting)


@require_POST
def delete_comment(request, posting_id, comment_id):
    posting = get_object_or_404(Posting, id=posting_id)
    comment = get_object_or_404(Comment, id=comment_id)
    comment.delete()
    return redirect(posting)