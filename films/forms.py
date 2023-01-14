from django import forms

from .models import *

class TagForm(forms.ModelForm):
    """Форма для створення тега"""
    class Meta:
        model = Tag
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(attrs={'class': 'input-char'})
        }


class FilmForm(forms.ModelForm):
    """Форма для створення фільму"""
    class Meta:
        model = Film
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(attrs={'class': 'input-char'}),
            'image': forms.FileInput(attrs={'class': 'input-file'}),
            'text': forms.Textarea(attrs={'id': 'add-comm-text', 'cols': 55, 'rows': 15}),
            'duration': forms.NumberInput(attrs={'class': 'input-micro'}),
            'url': forms.TextInput(attrs={'class': 'input-char'}),
            'country': forms.Select(attrs={'class': 'input-micro'}),
            'tag1': forms.Select(attrs={'class': 'input-micro'}),
            'tag2': forms.Select(attrs={'class': 'input-micro'}),
        }


class CommentForm(forms.ModelForm):
    """Форма для створення коментаря"""
    def __init__(self, *args, **kwargs):
        film_id = kwargs.pop('film_id')
        user_id = kwargs.pop('user_id')
        super().__init__(*args, **kwargs)
        self.fields['film'].initial = Film.objects.get(id=film_id)
        self.fields['author'].initial = CustomUser.objects.filter(id=user_id)[0]

    class Meta:
        model = Comment
        fields = ['film', 'title', 'text', 'author']
        widgets = {
            'film': forms.TextInput(attrs={'type': 'hidden'}),
            'author': forms.TextInput(attrs={'type': 'hidden'}),
            'title': forms.TextInput(attrs={'id': 'add-comm-title'}),
            'text': forms.Textarea(attrs={'id': 'add-comm-text', 'cols': 60, 'rows': 10}),
        }





