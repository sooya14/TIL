from django import forms
from .models import Article

# forms.Form => Data 입력 및 검증 

# ModelForm
class ArticleModelForm(forms.ModelForm):
    # 1. Data 검증 
    # 2. HTML 생성 
    title = forms.EmailField(min_length=3, required=False)  # 최소한 3글자는 써야한다. 
    class Meta:
        model = Article
        fields = '__all__'