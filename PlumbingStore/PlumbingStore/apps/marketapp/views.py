from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView

from .models import Advertisment, Feedback


class MarketHome(ListView):
    model = Advertisment
    template_name = 'marketapp/markethome.html'
    context_object_name = 'advert'


class AdvertDetail(DetailView):
    model = Advertisment
    template_name = 'marketapp/advert.html'
    context_object_name = 'advert'
    pk_url_kwarg = 'adv_pk'
