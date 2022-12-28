from django.shortcuts import render
from django.views.generic import View

from marketapp.models import Advertisment, Feedback, Company
from marketapp.forms import CreateFeedbackForm
from utils import AddContextMixin


class FeedbackSection(AddContextMixin, View):

    template_name = 'marketapp/feedback-section.html'
    form_class = CreateFeedbackForm

    def _find_feedbacks(self, slug=None):
        self.slug = slug
        models_to_search = [Advertisment, Company]
        for Object in models_to_search:
            try:
                Object.objects.get(slug=slug)
            except:
                continue
            else:
                self.object = Object

        feedbacks = Feedback.objects.filter(content_object=self.object)
        return feedbacks

    def get(self, request, *args, **kwargs):
        feedbacks = self._find_feedbacks(slug=self.kwargs.get('slug'))

        self.context = {
            'object_slug': self.slug,
            'form': self.form_class,
            'feedbacks': feedbacks,
            'menu': self.add_context()
        }
        return render(request, self.template_name, self.context)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.instance.user = self.request.user
            form.instance.content_object = self.object
            form.save()
            self.object.rating = get_object_rating(self.object)

        return render(request, self.template_name, self.context)