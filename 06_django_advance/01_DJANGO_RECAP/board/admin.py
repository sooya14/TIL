from django.contrib import admin
from .models import Article

# Register your models here.
class ArticleModelAdmin(admin.ModelAdmin):
    list_display = 'id', 'title'
    

admin.site.register(Article, ArticleModelAdmin)  # admindp 모델을 등록/ get_absolute_url 를 정의했기 때문에 '사이트보기'를 할 수 있다. 