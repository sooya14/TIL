from django.shortcuts import render, redirect, get_object_or_404
from .models import Question, Choice
from .forms import ChoiceModelForm
from django.views.decorators.http import require_GET, require_POST, require_http_methods



def question_detail(request, question_id):
    question = get_object_or_404(Question, id=question_id)
    return render(request, 'poll/question_detail.html', {
        'question': question,
    })


def upvote(request, question_id):
    question = get_object_or_404(Question, id=question_id)
    choice = ChoiceModelForm(request.POST, instance=question)

    

    
    return redirect('poll:question_detail', question_id)