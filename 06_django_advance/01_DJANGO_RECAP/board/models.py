from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=100, null=False)  # 비울거면 null = Ture / 기본값이 False
    content = models.TextField()
    