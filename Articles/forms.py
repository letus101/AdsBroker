from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['name', 'price', 'description', 'photo1', 'photo2', 'photo3', 'phone_number', 'category', 'ville']
