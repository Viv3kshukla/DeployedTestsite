from django import forms
from .models import Data

class Form(forms.ModelForm):
    class Meta:
        model=Data
        fields=[
            'primary_field',
            'first_field',
            'second_field',
            'third_field',
        ]