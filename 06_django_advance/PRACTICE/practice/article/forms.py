from django import forms ## 
from .models import Article, Comment ##


class ArticleModelForm(forms.ModelForm): ##
    title = forms.CharField(min_length=2) ##
        
    class Meta:
        model = Article
        fields = '__all__'

class CommentModelForm(forms.ModelForm):
    content = forms.CharField(min_length=2, max_length=200) ## 
    class Meta:
        model = Comment
        fields = ('content',)  # 사용자가 html 에서 받아서 입력할 수 있는 것은 content 만 

    