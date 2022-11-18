from django.shortcuts import render
from django.urls import reverse_lazy
from usersapp.models import User
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
from django.http import HttpResponse

from .models import Advertisment, Feedback
from .forms import CreateAdvertForm


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

#TODO: Убрать баг, хз как, ебать
class CreateAdvert(CreateView):
    form_class = CreateAdvertForm
    template_name = 'marketapp/createadvert.html'
    context_object_name = 'advert'
    success_url = reverse_lazy('adverts/')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = User.objects.filter(email=self.request.user)[0].id
        context = self.request.POST.copy()
        context['user'] = user
        return context
