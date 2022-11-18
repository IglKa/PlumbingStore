from .models import Advertisment
from django import forms


class CreateAdvertForm(forms.ModelForm):
    class Meta:
        model = Advertisment
        fields = ['category', 'title',
                  'description', 'image',
                  ]
