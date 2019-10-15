from django import forms
from .models import Question, Choice



class ChoiceModelForm(forms.ModelForm):
    CHOICES = [
        ('한식', '한식이다'), # request.POST 에 넘어오는 데이터는 '한식'이고, '한식이다'는 사용자한테 보이는 것
        ('중식', '중식이다'), 
        ('양식', '양식이다'),
        ]
    content = forms.ChoiceField(choices=CHOICES)
    class Meta:
        model = Choice
        fields = ('content',)  # 그래야지 사용자가 투표수를 조작하지 않을 수 있다. 

