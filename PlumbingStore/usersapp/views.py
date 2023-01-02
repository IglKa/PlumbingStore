from django.urls import reverse_lazy
from django.views.generic import DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

from django.contrib.auth.views import LoginView, LogoutView

from .forms import UserForm
from .models import User


class ProfileView(LoginRequiredMixin, DetailView):
    """ User Profile Page"""
    model = User
    template_name = 'usersapp/profile.html'
    context_object_name = 'profile'


class UserCreation(CreateView):
    template_name = 'usersapp/registration.html'
    form_class = UserForm
    success_url = reverse_lazy('usersapp:login')

class UserLogin(LoginView):
    template_name = 'usersapp/login.html'

class UserLogout(LogoutView):
    pass
