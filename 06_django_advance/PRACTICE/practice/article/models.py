from django.db import models
from django.urls import reverse ##

class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True) ##
    updated_at = models.DateTimeField(auto_now=True) ##

    def get_absolute_url(self):
        return reverse("article:article_detail", kwargs={"article_id": self.pk}) ##
    

class Comment(models.Model):
    content = models.TextField()
    article = models.ForeignKey(Article, on_delete=models.CASCADE) ##


