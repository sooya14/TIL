from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_http_methods, require_GET, require_POST

from django.contrib.auth.decorators import login_required
from .forms import CommentModelForm, PostingModelForm
from .models import Comment, Posting

@require_GET
def posting_list(request):
    postings = Postings.objects.all()
    return render(request, 'postings/posting_list.html',
    {
        'postings': postings,
    })

@require_GET
def posting_detail(request, posting_id):
    posting = get_object_or_404(Posting, id=posting_id)
    # comment = 
    return render(request, 'postings/posting_detail.html',{
        'posting': posting,
    })

@login_required
@require_http_methods(['POST', 'GET'])
def create_posting(request):
    if request.method == 'POST':
        form = PostingModelForm(request.POST)
        if form.is_valid():
            posting = form.save()
            return redirect(posting)
    else:
        form = PostingModelForm()
    return render(request, 'postings/posting_list.html', {
                'form':form,
            }) 
    

@login_required
@require_http_methods(['GET', 'POST'])
def update_posting(request, posting_id):
    posting = get_object_or_404(Posting, id=posting_id)
    if request.method =='POST':
        form = PostingModelForm(request.POST, instance=posting)
        if form.is_valid():
            posting = form.save()
            return redirect(posting)
    else:
        form = PostingModelForm(instance=posting)
    return render(request, 'postings/posting')


def delete_posting(request, posting_id):
    pass

def create_comment(request, posting_id):
    pass

def delete_comment(request, posting_id, comment_id):
    pass
