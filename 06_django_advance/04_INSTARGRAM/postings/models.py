from django.db import models
from django.urls import reverse
from django_extensions.db.models import TimeStampedModel  # django_extensions 를 설치해야만 가능 
from django.contrib.auth import get_user_model

from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFit  # 원본을 크기에 맞춰서 줄여준다. / ResizeToFill: 사이즈에 맞게 자른다. 


# user 는 절대 import 하는 것이 아니라 가져오는 것
User = get_user_model()

class HashTag(TimeStampedModel):  # created 랑 modified 가 자동으로 생성된다. 
    content = models.CharField(max_length=20, unique=True)  # unique=True => 똑같은 해쉬태그가 달리면 db에 저장을 하지 않는다. 


class Posting(TimeStampedModel):

    like_users = models.ManyToManyField(User, related_name='like_posts')  # 컬럼이 추가되는 것이 아니라 테이블이 생성된다. / posting 과 user 을 연결해준다.
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='postings')
    hashtags = models.ManyToManyField(HashTag, blank=True, related_name='postings')
    content = models.CharField(max_length=140)

    class Meta:
        ordering = ('-created',)

    def get_absolute_url(self):
        return reverse("postings:posting_detail", kwargs={"posting_id": self.pk})
    


class Image(models.Model):
    posting = models.ForeignKey(Posting, on_delete=models.CASCADE, related_name='images')  
    # file = models.ImageField()
    file = ProcessedImageField(
        processors=[ResizeToFit(600, 600, mat_color=(45, 45, 45))], # 0, 0, 0 이 검은색 / 45, 45, 45 회색
        upload_to='postings/images',  # 그 밑에 여기에다가 넣겠다고 설정
        format='JPEG', 
        options={'quality': 90},
    )

    # p.images_set.all()  => related_name 이 defult
    # p.images.all()  => related_name 이 imnage


class Comment(TimeStampedModel):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')  # related_name : 남(user)이 나를 어떻게 부를까? 
    posting = models.ForeignKey(Posting, on_delete=models.CASCADE, related_name='comments')
    content = models.CharField(max_length=140)


