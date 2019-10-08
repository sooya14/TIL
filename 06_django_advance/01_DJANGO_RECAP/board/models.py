from django.db import models
from django.urls import reverse

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=100, null=False)  # 비울거면 null = Ture / 기본값이 False
    content = models.TextField()
    
    # detail 페이지를 만들것 같을 때 사용 / 견적서에 따로 반영이 되지 않는다. / model 에 코드를 바꾸면 견적을 한번 돌려보세요용 
    def get_absolute_url(self):
        return reverse("board:detail", kwargs={"id": self.pk})

    
    