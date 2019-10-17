from django.urls import path ## 
from . import views  ##

app_name = 'article'

urlpatterns = [
    path('', views.article_list, name='article_list'),
    path('<int:article_id>/detail/', views.article_detail, name='article_detail'),
    path('new/', views.new_article, name='new_article'),
    
]


