from django import forms
from .models import Author


class AddAuthor(forms.ModelForm):
    class Meta:
        model = Author
        fields = ("name", "surname", "patronymic")


class EditAuthor(forms.ModelForm):
    class Meta:
        model = Author
        fields = ("name", "surname", "patronymic")
