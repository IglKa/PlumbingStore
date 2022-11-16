from .models import Advertisment
from django import forms


class CreateAdvert(forms.ModelForm):
    class Meta:
        model = Advertisment
        fields = ['category', 'title',
                  'description', 'image',
                  ]
