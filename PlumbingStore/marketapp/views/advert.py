from django.views import View
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView
from django.views.generic.detail import SingleObjectMixin

from marketapp.models import Advertisment, Feedback, Company
from marketapp.forms import CreateFeedbackForm, RatingForm
from utils import AddContextMixin
# I had to separate class AdvertPage(SingleObjectMixin, CreateView):
# Because this implementation was causing a lot of problems.
# Now the problem is, that this code is giving SQLqueries for each author of comment.
# TODO: Refactor


class AdvertContextView(AddContextMixin, SingleObjectMixin, ListView):
    """Will search for context to advert page"""
    template_name = 'marketapp/advert.html'

    def get(self, request, *args, **kwargs):
        # We need to find the SingleObject that we are working with
        # so we can find it's comments later.
        self.object = self.get_object(queryset=Advertisment.objects.all())
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['advert'] = self.object
        context['menu'] = self.add_context()
        context['form'] = CreateFeedbackForm()
        return context

    def get_queryset(self):
        # Finding set of feedbacks for advertisment.
        return self.object.feedback_set.all()


class CreateFeedbackView(LoginRequiredMixin, CreateView):
    """Feedback form class for advert page"""
    model = Feedback
    form_class = CreateFeedbackForm
    template_name = 'marketapp/advert.html'

    def form_valid(self, form, **kwargs):
        form.instance.company = self.request.user.company
        form.instance.advert = Advertisment.objects.get(slug=self.kwargs.get('slug'))
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('marketapp:advert-page', kwargs={'slug': self.kwargs.get('slug')})


class AdvertPage(View):
    """Advertisment page implementation"""
    def get(self, request, *args, **kwargs):
        # call context class with as_view() method
        view = AdvertContextView.as_view()
        return view(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        # call form class with as_view() method
        view = CreateFeedbackView.as_view()
        return view(request, *args, **kwargs)
