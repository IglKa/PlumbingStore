from django import forms

from .models import Feedback, Advertisment, Rating


class RatingForm(forms.ModelForm):
    star = forms.ModelChoiceField(
        queryset=Rating.objects.all(), widget=forms.RadioSelect(), empty_label=None
    )
    class Meta:
        model = Rating
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
