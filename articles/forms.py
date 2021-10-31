from django import forms
from .models import Article


class CommentForm(forms.Form):
    name = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)

class  ArticleForm(forms.ModelForm):
    article_name = forms.CharField(label='Название статьи')
    article_text = forms.CharField(label='Текст статьи')
    class Meta:
        model = Article
        #fields = '__all__'
        fields = ('article_name', 'article_text','article_img')
        #exclude = ('article_date')