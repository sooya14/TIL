from django.urls import path
from . import views

app_name = 'todos'  # 필요없음... 

urlpatterns = [
    path('', views.create_todo),
]
