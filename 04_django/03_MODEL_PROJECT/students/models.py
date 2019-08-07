from django.db import models

# 테이블 시트 생성의 영역 
class Student(models.Model):
    # 얻어걸리도록 의도한다. 
    name = models.CharField(max_length=10)
    email = models.CharField(max_length=10)
    github_id = models.CharField(max_length=50)
    age = models.IntegerField()

class Menu(models.Model):
    # name: 메뉴이름 => STRING
    # price: 가격 => FLOAT
    # category: 카테고리 => STRING
    # 모델링 => 견적 => 테이블생성 => CRUD
    name = models.CharField(max_length=10)
    price = models.FloatField(default=0)
    category = models.CharField(max_length=10)