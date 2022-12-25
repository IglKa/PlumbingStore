from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView
from django.views.generic.detail import SingleObjectMixin

from marketapp.models import Advertisment, Feedback
from marketapp.forms import CreateFeedbackForm
from utils import AddContextMixin


class FeedbackSectionView(AddContextMixin, SingleObjectMixin, ListView):
    template_name = 'marketapp/feedback-section.html'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object(queryset=Advertisment.objects.all())
        return super().get(request, *args, **kwargs)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = self.add_context()
        context['form'] = CreateFeedbackForm()
        return context

    def get_queryset(self):
        return self.object.feedback_set.all()