# from django.contrib import admin
from django.urls import path 
from . import views

# makemigrtion 하기 전에 app_name 이랑 urlpatterns 만 설정해놓아야한다. 
app_name = 'classroom'

urlpatterns = [
    path('', views.index, name='index'), 

    # 결국에는 name 으로 부르는 것이고 앞에 url 로 요청해서 뒤에 views 의 함수를 실행하는 것
    
    # 글 쓰기 
    path('student/new/', views.new, name='new'), 
    # 글 저장
    path('student/create/', views.create, name='create'),
    # 글 리스트 
    path('student/', views.list, name='list'),
    
    path('student/<int:id>/', views.detail, name='detail'),

    path('student/<int:id>/delete/', views.delete, name="delete"),
    path('student/<int:id>/edit/', views.edit, name='edit'),

    path('student/<int:id>/update/', views.update, name='update'),

    


]