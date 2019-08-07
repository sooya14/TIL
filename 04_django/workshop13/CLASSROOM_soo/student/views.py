from django.shortcuts import render

# Create your views here.


def student(request, name):
    students = {
        '홍길동': 1, 
        '김길동': 2, 
        '박길동': 28,
    }
    return render(request, 'student.html', {
            'age': students[name],
            'name': name,

    })