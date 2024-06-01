from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['name', 'price', 'description', 'photo1', 'photo2', 'photo3', 'phone_number', 'category', 'ville']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'border border-gray-300 rounded-lg p-2 focus:outline-none focus:border-indigo-500'}),
            'price': forms.NumberInput(attrs={'class': 'border border-gray-300 rounded-lg p-2 focus:outline-none focus:border-indigo-500'}),
            'description': forms.Textarea(attrs={'class': 'border border-gray-300 rounded-lg p-2 focus:outline-none focus:border-indigo-500'}),
            'photo1': forms.ClearableFileInput(attrs={'class': 'border border-gray-300 rounded-lg p-2 focus:outline-none focus:border-indigo-500'}),
            'photo2': forms.ClearableFileInput(attrs={'class': 'border border-gray-300 rounded-lg p-2 focus:outline-none focus:border-indigo-500'}),
            'photo3': forms.ClearableFileInput(attrs={'class': 'border border-gray-300 rounded-lg p-2 focus:outline-none focus:border-indigo-500'}),
            'phone_number': forms.TextInput(attrs={'class': 'border border-gray-300 rounded-lg p-2 focus:outline-none focus:border-indigo-500'}),
            'category': forms.Select(attrs={'class': 'border border-gray-300 rounded-lg p-2 focus:outline-none focus:border-indigo-500'}),
            'ville': forms.Select(attrs={'class': 'border border-gray-300 rounded-lg p-2 focus:outline-none focus:border-indigo-500'}),
        }
