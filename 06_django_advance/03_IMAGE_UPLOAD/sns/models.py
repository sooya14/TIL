from django.db import models
from django.urls import reverse
from django.conf import settings # MASTER_APP/settings.py


# Create your models here.
class Posting(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField()
    icon = models.CharField(max_length=30, default='')
    image = models.ImageField(blank=True) # $ pip install pillow 를 해야지 사용할 수 있다.  # 비워있을 수도 있다. / null 보단 blank 를 더 많이 쓴다. 
    created_at = models.DateTimeField(auto_now_add=True)  # 추가될 때만
    updated_at = models.DateTimeField(auto_now=True) # 수정, save 할 때마다 바뀔떄 마다 

    class Meta:
        ordering = ['-created_at', ]  # created_at 을 desending 내림차순으로 

    # detail 페이지를 쓸 거라면 만들어요
    def get_absolute_url(self):
        return reverse("sns:posting_detail", kwargs={"posting_id": self.pk})

    def __str__(self):
        return f'{self.pk}: {self.content}'


class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # related_name 이 없으면, posting.comment_set 이고, 아래와 같다면, posting.comments
    posting = models.ForeignKey(Posting, on_delete=models.CASCADE, related_name='comments')  # posting 이 comment 를 부를 때 이렇게 이름이 바뀐다. 
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at',]

    def __str__(self):
        return f'{self.id}: {self.content[:20]}'
