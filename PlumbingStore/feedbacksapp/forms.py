from django import forms

from .models import Feedback


class CreateFeedbackForm(forms.ModelForm):
    rating = forms.ChoiceField(widget=forms.RadioSelect,
                               choices=Feedback.Star.choices
                               )
    class Meta:
        model = Feedback
        fields = ['text', 'image', 'rating']
