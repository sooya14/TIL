from django.shortcuts import render, redirect, get_object_or_404 
from .models import Classroom

# Create your views here.

def index(request):
    return render(request, 'classroom/index.html')

def new(request):
    return render(request, 'classroom/new.html')

def create(request):
    student = Classroom()
    student.name = request.POST.get('name')
    student.age = request.POST.get('age')
    student.major = request.POST.get('major')
    student.save()
    return redirect('classroom:list')

def list(request):
    students = Classroom.objects.all()
    return render(request, 'classroom/list.html', {
        'classrooms': students,
    })

def detail(request, id):
    student = get_object_or_404(Classroom, id=id)
    return render(request, 'classroom/detail.html', {
        'student': student,
    })

def delete(request, id):
    student = get_object_or_404(Classroom, id=id)
    student.delete()
    return redirect('classroom:list')

def edit(request, id):
    student = get_object_or_404(Classroom, id=id)
    return render(request, 'classroom/edit.html', {
        'student': student,
    })

def update(request, id):
    student = get_object_or_404(Classroom, id=id)
    student.name = request.POST.get('name')
    student.age = request.POST.get('age')
    student.major = request.POST.get('major')
    student.save()
    return redirect('classroom:list')

