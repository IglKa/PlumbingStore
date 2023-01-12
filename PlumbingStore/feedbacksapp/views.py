from django.shortcuts import render
from django.views.generic import View
from django.contrib.auth.decorators import login_required

from .forms import CreateFeedbackForm
from .services import get_feedback_section_context, get_model_instance, end_feedback_post_logic


class FeedbackSection(View):
    """
    Feedback section for different objects

    This is something like 'generic' view, so I implement it that it will find
    the model and feedbacks for this model by having only slug.
    """

    template_name = 'feedbacks/feedback-section.html'
    form_class = CreateFeedbackForm

    def _get_model_instance(self, slug):
        self.model_instance = get_model_instance(slug)
        return self.model_instance

    def get(self, request, **kwargs):
        slug = kwargs.get('slug')
        return render(request, self.template_name, get_feedback_section_context(slug=slug, form=self.form_class))

    @login_required
    def post(self, request, **kwargs):
        form = self.form_class(request.POST)
        slug = kwargs.get('slug')
        if form.is_valid():
            # will create feedback object and update model[Advert, Company] rating.
            end_feedback_post_logic(self.request.user, form, self._get_model_instance(slug))
        return render(request, self.template_name, get_feedback_section_context(slug=slug, form=self.form_class))
