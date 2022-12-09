from django.views import View
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView
from django.views.generic.detail import SingleObjectMixin

from marketapp.models import Advertisment, Feedback, Company
from marketapp.forms import CreateFeedbackForm


class AdvertContextView(SingleObjectMixin, ListView):
    template_name = 'marketapp/advert.html'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object(queryset=Advertisment.objects.all())
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['advert'] = self.object
        context['form'] = CreateFeedbackForm()
        return context

    def get_queryset(self):
        return self.object.feedback_set.all()


class CreateFeedbackView(LoginRequiredMixin, CreateView):
    model = Feedback
    form_class = CreateFeedbackForm
    template_name = 'marketapp/advert.html'

    def form_valid(self, form, **kwargs):
        form.instance.user = self.request.user
        form.instance.advert = Advertisment.objects.get(slug=self.kwargs.get('slug'))
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('marketapp:advert_page', kwargs={'slug': self.kwargs.get('slug')})


class AdvertPage(View):
    def get(self, request, *args, **kwargs):
        view = AdvertContextView.as_view()
        return view(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        view = CreateFeedbackView.as_view()
        return view(request, *args, **kwargs)
