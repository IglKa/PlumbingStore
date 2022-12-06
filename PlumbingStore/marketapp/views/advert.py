from django.views.generic.detail import SingleObjectMixin
from django.views.generic.edit import CreateView
from django.shortcuts import reverse
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

from marketapp.models import Advertisment, Feedback, Company
from marketapp.forms import CreateFeedbackForm
import utils


class CreateAdvert(LoginRequiredMixin, CreateView):
    model = Advertisment
    fields = ['category', 'title',
              'description', 'image'
              ]
    template_name = 'marketapp/createadvert.html'
    success_url = reverse_lazy('marketapp:homepage')

    def form_valid(self, form):
        # Adds User to Advertisment
        form.instance.user = self.request.user
        form.save(commit=False)
        slug = utils.SlugHandle(user=self.request.user, title=form.instance.title)
        form.instance.slug = slug.fill_slug()
        return super().form_valid(form)


class AdvertPage(CreateView, SingleObjectMixin):
    """
    View for the advertisment page. It will render the page with:
    advertisment information;
    feedbacks;
    form to add feedbacks.
    """
    template_name = 'marketapp/advert.html'
    form_class = CreateFeedbackForm

    def get(self, request, slug, *args, **kwargs):
        self.obj = super().get_object(queryset=Advertisment.objects.filter(slug=slug))
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.form_class
        context['advert'] = self.obj
        context['feedback'] = Feedback.objects.filter(advert=self.obj)
        return context

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.advert = self.model
        return super().form_valid(form)
