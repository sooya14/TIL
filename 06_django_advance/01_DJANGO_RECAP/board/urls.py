from django.urls import path
from . import views

app_name = 'board'

urlpatterns = [
    # path('', views.index, name='index'), # /board/ == board:index

    # Read 글 목록(list) render
    path('articles/', views.article_list, name='article_list'),
    # Read 글 상세 (detail) render
    path('articles/<int:article_id>/', views.article_detail, name='article_detail'),

    # Create 글 쓰기(new) render
    path('articles/new/', views.new_article, name='new_articl'),
    # Create 글 저장 (create) 
    # 함수를 불러오는 것이 아니라 create url 로 이동하는 것 
    # path('articles/create/', views.create, name='create'),

    # Update 글 수정쓰기 (edit) render
    path('articles/<int:article_id>/edit/', views.edit_article, name='edit_article'),
    # Update 글 실제수정 (update)
    # path('articles/<int:id>/update/', views.update, name='update'),

    # Delete 글 삭제 (delete)
    path('articles/<int:article_id>/delete/', views.delete_article, name='delete_article'),

    # Comment Create
    path('articles/<int:article_id>/comments/new/', views.new_comment, name='new_comment'),
]
    