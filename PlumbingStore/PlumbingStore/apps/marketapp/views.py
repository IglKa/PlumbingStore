from django.shortcuts import redirect
from django.urls import reverse_lazy
from usersapp.models import User
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, FormView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Advertisment, Feedback


class MarketHome(ListView):
    model = Advertisment
    template_name = 'marketapp/markethome.html'
    context_object_name = 'advert'


class AdvertDetail(DetailView):
    model = Advertisment
    template_name = 'marketapp/advert.html'
    context_object_name = 'advert'
    #TODO: Сделать поиск по slug
    pk_url_kwarg = 'adv_pk'


class CreateAdvert(LoginRequiredMixin, CreateView):
    model = Advertisment
    fields = ['category', 'title',
              'description', 'image'
              ]
    template_name = 'marketapp/createadvert.html'
    success_url = reverse_lazy('marketapp:homepage')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

