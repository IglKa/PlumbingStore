from django import forms

from .models import Feedback, Advertisment


class CreateAdvertForm(forms.ModelForm):
    class Meta:
        model = Advertisment
        fields = ['category', 'title',
                  'description', 'image']


class CreateFeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['text', 'image']
