from django.shortcuts import render
from django.views.generic import DetailView

from .models import Company


class CompanyDetail(DetailView):
    model = Company
    template_name = 'shopapp/company.html'
    context_object_name = 'company'
