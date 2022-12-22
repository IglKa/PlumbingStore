from django import forms

from .models import Feedback, Advertisment, Star


class RatingForm(forms.ModelForm):
    star = forms.ModelChoiceField(
        queryset=Star.objects.all(), widget=forms.RadioSelect(), empty_label=None
    )
    class Meta:
        model = Star
        fields = ('star', )


class CreateAdvertForm(forms.ModelForm):
    class Meta:
        model = Advertisment
        fields = ['category', 'title',
                  'description', 'image']


class CreateFeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['text', 'image']
