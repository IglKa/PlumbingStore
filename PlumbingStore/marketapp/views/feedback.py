from django.shortcuts import render
from django.views.generic import View

from marketapp.forms import CreateFeedbackForm
from utils import AddContextMixin
from marketapp.businesslogic import find_feedbacks, get_model_instance, update_rating

class FeedbackSection(AddContextMixin, View):
    """Feedback section for different objects"""
    template_name = 'marketapp/feedback-section.html'
    form_class = CreateFeedbackForm

    def _get_context(self, slug):
        self.context = {
            'object_slug': slug,
            'feedbacks': find_feedbacks(get_model_instance(slug)),
            'form': self.form_class,
            'menu': self.add_context()
        }
        return self.context

    def get(self, request, *args, **kwargs):
        slug = kwargs.get('slug')
        return render(request, self.template_name, self._get_context(slug))

    def post(self, request, *args, **kwargs):

        form = self.form_class(request.POST)
        slug = kwargs.get('slug')
        model_instance = get_model_instance(slug)
        if form.is_valid():
            form.instance.user = self.request.user
            form.instance.content_object = model_instance
            form.save()
            update_rating(model_instance)
            form.save()
            return render(request, self.template_name, self._get_context(slug))
