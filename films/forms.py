from django import forms

from .models import *

class TagForm(forms.ModelForm):
    """Форма для створення тега"""
    class Meta:
        model = Tag
        fields = '__all__'


class FilmForm(forms.ModelForm):
    """Форма для створення фільму"""
    class Meta:
        model = Film
        fields = '__all__'


class CommentForm(forms.ModelForm):
    """Форма для створення коментаря"""
    def __init__(self, *args, **kwargs):
        film_id = kwargs.pop('film_id')
        user_id = kwargs.pop('user_id')
        super().__init__(*args, **kwargs)
        self.fields['film'].initial = Film.objects.get(id=film_id)
        self.fields['author'].initial = CustomUser.objects.get(id=user_id)

    class Meta:
        model = Comment
        fields = ['film', 'title', 'text', 'author']
        widgets = {
            'film': forms.TextInput(attrs={'type': 'hidden'}),
            'author': forms.TextInput(attrs={'type': 'hidden'}),
        }


