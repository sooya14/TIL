from django import forms
from .models import Article, Comment

# forms.Form => Data 입력 및 검증 
# forms.ModelForm => Data 입력/검증 + HTML 생성 


class ArticleModelForm(forms.ModelForm):
    # 1. Data 검증 
    # 2. HTML 생성 
    # title = forms.EmailField(min_length=3, required=False)  # 최소한 3글자는 써야한다. 
    title = forms.CharField(min_length=2, max_length=100)  


    class Meta:
        model = Article
        fields = '__all__'

# model 과 form 은 한 세트이다. 시작할때 자동적으로 만들기 

class CommentModelForm(forms.ModelForm):
    content = forms.CharField(min_length=2, max_length=200)  # 200 을 넘는지 검증 하는 용도 

    class Meta:
        model = Comment
        fields = '__all__'

