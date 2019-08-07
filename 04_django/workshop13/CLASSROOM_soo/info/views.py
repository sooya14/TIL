from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, HttpResponse

def info(request):
    teacher = 'NAME'
    students = ['홍길동', '김길동', '박길동']

    return render(request, 'info.html', {
        'teacher': teacher, 
        'students': students, 
    })

