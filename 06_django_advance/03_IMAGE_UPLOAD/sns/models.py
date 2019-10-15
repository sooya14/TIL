from django.db import models
from django.urls import reverse


# Create your models here.
class Posting(models.Model):
    content = models.TextField()
    icon = models.CharField(max_length=30, default='')
    image = models.ImageField(blank=True) # $ pip install pillow 를 해야지 사용할 수 있다.  # 비워있을 수도 있다. / null 보단 blank 를 더 많이 쓴다. 
    created_at = models.DateTimeField(auto_now_add=True)  # 추가될 때만
    updated_at = models.DateTimeField(auto_now=True) # 수정, save 할 때마다 바뀔떄 마다 

# detail 페이지를 쓸 거라면 만들어요
    def get_absolute_url(self):
        return reverse("sns:posting_detail", kwargs={"posting_id": self.pk})

    def __str__(self):
        return f'{self.pk}: {self.content}'

