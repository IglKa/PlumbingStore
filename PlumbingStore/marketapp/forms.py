from django import forms

from .models import Feedback, Advertisment, Follow


class CreateAdvertForm(forms.ModelForm):
    class Meta:
        model = Advertisment
        fields = ['category', 'title',
                  'description', 'image']


class CreateFeedbackForm(forms.ModelForm):
    rating = forms.ChoiceField(widget=forms.RadioSelect,
                               choices=Feedback.Star.choices
                               )

    class Meta:
        model = Feedback
        fields = ['text', 'image', 'rating']


class FollowCompanyForm(forms.ModelForm):
    class Meta:
        model = Follow
        fields = []
