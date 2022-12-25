from django import forms

from .models import Feedback, Advertisment, Star


class CreateAdvertForm(forms.ModelForm):
    class Meta:
        model = Advertisment
        fields = ['category', 'title',
                  'description', 'image']


class CreateFeedbackForm(forms.ModelForm):
    star_given = forms.ModelChoiceField(queryset=Star.objects.all(),
                                        widget=forms.RadioSelect,
                                        empty_label=None)

    class Meta:
        model = Feedback
        fields = ['text', 'image', 'star_given']
