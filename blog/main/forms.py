from django import forms
from .models import Comment


class AddArticle(forms.Form):
    title = forms.CharField(max_length=255, label='заголовок')
    content = forms.CharField(widget=forms.Textarea(), label='содержание статьи')


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']




