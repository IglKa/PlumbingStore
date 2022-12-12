from django.views.generic import TemplateView, DetailView, ListView
from django.views.generic.detail import SingleObjectMixin
from django.views.generic.edit import CreateView
from django.contrib.auth import login, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render

from .forms import UserForm
from .models import User
from marketapp.models import Advertisment
# TODO: Исправить баг со входом


class ProfileView(LoginRequiredMixin, DetailView):
    """ User Profile Page"""
    model = User
    template_name = 'registration/profile.html'
    context_object_name = 'profile'


class UserAdvertsView(SingleObjectMixin, ListView):
    """User advertisments"""
    template_name = 'registration/user-adverts.html'

    def get(self, request, *args, **kwargs):
        # We need to find user and save it till later
        self.object = self.get_object(queryset=User.objects.filter(pk=kwargs.get('pk')))
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.object
        return context

    def get_queryset(self):
        # All user adverts
        return self.object.advertisment_set.all()


class UserCreation(CreateView):
    template_name = 'registration/registration.html'
    form_class = UserForm
    success_url = 'marketapp:homepage'

    def form_valid(self, form):
        form.save()
        email = self.request.POST['email']
        password = self.request.POST['password']
        user = authenticate(self.request, username=email, password=password)
        login(self.request, user=user)
        return redirect(self.success_url)
