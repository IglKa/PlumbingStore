from django.db.models import QuerySet
from django.http import Http404
from django.shortcuts import render
from django.views.generic import View

from marketapp.models import Advertisment, Feedback, Company
from marketapp.forms import CreateFeedbackForm
from utils import AddContextMixin, get_object_rating


class FeedbackSection(AddContextMixin, View):
    """Feedback section for different objects"""
    template_name = 'marketapp/feedback-section.html'
    form_class = CreateFeedbackForm

    def _find_feedbacks(self, slug=None) -> QuerySet:
        """
        I think that this view will be something like 'generic'.
        It would find either Advertisment or Company (based on the given slug).
        """

        self.slug = slug
        models_to_search = [Advertisment, Company]
        for Object in models_to_search:
            try:
                setattr(self, 'object', Object.objects.get(slug=self.slug))
            except:
                continue
            else:
                feedbacks = self.object.feedbacks.all()
            return feedbacks
        raise Http404

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