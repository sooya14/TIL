from django.db import models
# User < AbstractUser < AbstractBaseUser
from django.contrib.auth.models  import AbstractUser  
from django.conf import settings  # ManyToManyField 에서 AUTH_USER_MODEL 사용할라고 import
from faker import Faker

f = Faker()

class User(AbstractUser):  # 여기서 새로 만들어서 수정하면 된다. => user 모델을 확장을 할지 말지 모르겠지만 일단 이것을 쓰고 확장을 하든 말든
      
    fans = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='stars')  # m 대n 할 때 사용하는 field 
    # accounts app의 user 라고 해준다. 
    # ManyToManyField는 칼럼이 추가되는 것이 아니라 테이블이 추가된다. 

    def __str__(self):
        return self.username

    @classmethod
    def dummy(cls, n):
        for i in range(n):

            u = cls()  # u = User 랑 같은 것 
            u.username = f.first_name()
            u.set_password('1234qwer')
            u.save()

    # shell_plus
    # User.dummy(3)
    # star = User.objects.first()
    # fan1 = User.objects.get(id=3)
    # star.fans.add(fan1)