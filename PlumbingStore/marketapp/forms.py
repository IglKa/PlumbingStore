from django import forms

from .models import Feedback


class CreateFeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['text', 'image']
