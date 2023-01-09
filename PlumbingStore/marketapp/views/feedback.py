from django.shortcuts import render
from django.views.generic import View

import utils
from marketapp.forms import CreateFeedbackForm
from marketapp.services import get_model_instance, \
                                    update_rating, \
                                    find_feedbacks


class FeedbackSection(View):
    """Feedback section for different objects"""

    template_name = 'marketapp/feedback-section.html'
    form_class = CreateFeedbackForm

    def _get_context(self, slug):
        self.context = {
            'object_slug': slug,
            'feedbacks': find_feedbacks(get_model_instance(slug)),
            'form': self.form_class,
            'menu': utils.add_context()
        }
        return self.context

    def get(self, request, **kwargs):
        slug = kwargs.get('slug')
        return render(request, self.template_name, self._get_context(slug))

    def post(self, request, **kwargs):
        form = self.form_class(request.POST)
        slug = kwargs.get('slug')
        model_instance = get_model_instance(slug)
        if form.is_valid():
            form.instance.user = self.request.user
            form.instance.content_object = model_instance
            form.save()
            update_rating(model_instance)
        return render(request, self.template_name, self._get_context(slug))
