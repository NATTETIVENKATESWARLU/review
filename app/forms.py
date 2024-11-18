from django import forms
from app.models import *

class movie_add(forms.ModelForm):
    class Meta:
        model=movies
        fields="__all__"