from django.shortcuts import render
from django.views.generic import View
from django.contrib.auth.decorators import login_required

from .forms import CreateFeedbackForm
from .services import get_feedback_section_context, get_model_instance, end_feedback_post_logic



class FeedbackSection(View):
    """Feedback section for different objects"""

    template_name = 'marketapp/feedback-section.html'
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
            end_feedback_post_logic(request.user, form, self._get_model_instance(slug))
        return render(request, self.template_name, get_feedback_section_context(slug=slug, form=self.form_class))
