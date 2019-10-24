from django.db import models
from django.conf import settings  # 1. 만약 import가 되어 있다면, settings.AUTH_USER_MODEL
from django.contrib.auth import get_user_model # 2. 아무것도 import 가 안되어 있다면, 

User = get_user_model()  # 수경아 괄호써!!!!!!!!!!!!!!!!!!!!!!!!

class Article(models.Model):
    # ForeignKey => 인자 2개
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # 모델을 줄것같음.... 쌤피셜 
    title = models.CharField(max_length=200)
    content = models.TextField()
    # 내가 뭐라고 접근할지 = ....related_name= 남이 나를 뭐라고 부를지 
    like_users = models.ManyToManyField(User, related_name='like_articles')
