from .models import Articles
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea


class ArticlesForm(ModelForm):
    class Meta:
        model = Articles
        fields = ['title', 'anons', 'full_text', 'date']

        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control', 
                'placeholder': 'Title of the article'
            }),
            "anons": TextInput(attrs={
                'class': 'form-control', 
                'placeholder': 'Announcement of the article'
            }),
            "full_text": Textarea(attrs={
                'class': 'form-control', 
                'placeholder': 'The text of the article'
            }),
            "date": DateTimeInput(attrs={
                'class': 'form-control', 
                'placeholder': 'Date of publication'
            }),
        }



