from django.db import models
from django.urls import reverse
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser,
    PermissionsMixin)
from django.conf import settings

# Create your models here.

# class MyUserManager(BaseUserManager):
#     def create_user(self, email, nickname, password=None):
#         if not email:
#             raise ValueError('Users must have an email address')
 
#         user = self.model(
#             email=MyUserManager.normalize_email(email),
#             nickname=nickname,
#         )
 
#         user.set_password(password)
#         user.save(using=self._db)
#         return user
class UserManager(BaseUserManager):
    def create_user(self, email, nickname, password=None):
        """
        주어진 이메일, 닉네임, 비밀번호 등 개인정보로 User 인스턴스 생성
        """
        if not email:
            raise ValueError(('Users must have an email address'))

        user = self.model(
            email=self.normalize_email(email),
            nickname=nickname,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, nickname, last_name, first_name, password):
        """
        주어진 이메일, 닉네임, 비밀번호 등 개인정보로 User 인스턴스 생성
        단, 최상위 사용자이므로 권한을 부여한다. 
        """
        user = self.create_user(
            email=email,
            password=password,
            nickname=nickname,
        )

        user.is_admin = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True, verbose_name='이메일')
    name = models.CharField(max_length=20, verbose_name='이름')
    nickname = models.CharField(unique=True, max_length=20, verbose_name='닉네임',null=False, blank=False)
    item = models.CharField(blank=True, null=True, max_length=50, verbose_name='유저 물건')
    price = models.IntegerField(blank=True, null=True, verbose_name='물건가격')
    monthly_cost = models.IntegerField(blank=True, null=True)
    image = models.ImageField(blank=True, null=True, verbose_name='프로필사진')
    birth = models.DateTimeField(blank=True, null=True, verbose_name='생일')


    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = UserManager()
    USERNAME_FIELD = 'email'


    def get_full_name(self):
        # The user is identified by their email address
        return self.email
 
    def get_short_name(self):
        # The user is identified by their email address
        return self.email
 
    def __str__(self):
        return self.email
 
    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True
 
    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True


    

class User_history(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='history')
    payment_date = models.DateTimeField(auto_now_add=True)
    user_breakfast = models.IntegerField(blank=True, null = True)
    user_lunch = models.IntegerField(blank=True, null = True)
    user_dinner = models.IntegerField(blank=True, null = True)
    total_paid = models.IntegerField(blank=True, null = True)