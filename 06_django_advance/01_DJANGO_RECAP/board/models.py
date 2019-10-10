from django.db import models
from django.urls import reverse


class Article(models.Model):
    title = models.CharField(max_length=100, null=False)  # 비울거면 null = Ture / 기본값이 False
    content = models.TextField()
    
    # detail 페이지를 만들것 같을 때 사용 / 견적서에 따로 반영이 되지 않는다. / model 에 코드를 바꾸면 견적을 한번 돌려보세요용 
    def get_absolute_url(self):  # detail page 가 있을 때 
        return reverse("board:article_detail", kwargs={"article_id": self.pk})

class Comment(models.Model):
    content = models.CharField(max_length=200)  # CharField 는 max_length 가 필수 / 저장이 되는데 숫자 제한 잘라서 저장한다. 
    article = models.ForeignKey(Article, on_delete=models.CASCADE)  # 원본이 지워지면 부가정보도 같이 지워진다. / on_delete 뒤에 뭐라도 있어야한다. 
    # ForeignKey 덕분에 article_id 라고 하지 않아도 알아서 잡힌다. 
    # Article 과 순서 바꿀수 없다. 

    
    