from .models import Posting, Comment
from django import forms

class PostingModelForm(forms.ModelForm):
    title = forms.CharField(min_length=1)
    class Meta:
        model = Posting
        fields = '__all__'

class CommentModelForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('content',)