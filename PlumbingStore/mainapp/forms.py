from django import forms

from .models import Advertisment


class CreateAdvertForm(forms.ModelForm):
    class Meta:
        model = Advertisment
        fields = ['category', 'title',
                  'description', 'image']
