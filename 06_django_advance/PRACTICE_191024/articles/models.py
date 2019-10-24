from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()  ## 제발 괄호좀 ㅠㅠㅠ 

class Article(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    title = models.CharField(max_length=20)  ## 
    content = models.TextField()

    like_users = models.ManyToManyField(User, related_name='like_articles')


