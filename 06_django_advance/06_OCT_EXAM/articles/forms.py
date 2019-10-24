from django import forms  # 얘만 바로 django 에서 바로 꺼내면 된다. 
from .models import Article


# forms / models 앞은 s 가 붙고, Form / Model 은 안붙는다. 
# forms.ModelForm / models.Model
class ArticleForm(forms.ModelForm):  # ModelForm!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    class Meta:
        model = Article
        fields = ('title', 'content',)  # title 과 content 만 검증(is_valid)한다.