from django.contrib.auth.forms import UserCreationForm
from django import forms

from .models import *


class RegisterForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ["username", "password1", "password2", "dob", "email", "status", "about"]


class PagePostForm(forms.ModelForm):
    """Створити допис на сторінці"""
    def __init__(self, *args, **kwargs):
        user_id = kwargs.pop('user_id')
        super().__init__(*args, **kwargs)
        self.fields['author'].initial = CustomUser.objects.get(id=user_id)

    class Meta:
        model = PagePost
        fields = ["title", "image", "text", "author"]
        widgets = {
            'author': forms.TextInput(attrs={'type': 'hidden'}),
            }


class MessageForm(forms.ModelForm):
    """Форма для написання повідомлення"""
    def __init__(self, *args, **kwargs):
        user_id = kwargs.pop('user_id')
        super().__init__(*args, **kwargs)
        self.fields['author'].initial = CustomUser.objects.get(id=user_id)
    class Meta:
        model = Message
        fields = ["text", "author", "receiver"]
        widgets = {
            'author': forms.TextInput(attrs={'type': 'hidden'}),
            'text': forms.Textarea(attrs={'cols': 50, 'rows': 10}),
        }