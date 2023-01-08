from django.views.generic import DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login

from .models import User
from .forms import UserForm
# from .services import end_registration


class ProfileView(LoginRequiredMixin, DetailView):
    """ User Profile Page"""

    model = User
    template_name = 'usersapp/profile.html'
    context_object_name = 'profile'


class UserCreation(CreateView):
    template_name = 'usersapp/registration.html'
    form_class = UserForm
    success_url = reverse_lazy('marketapp:homepage')

    def form_valid(self, form):
        form.save()
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password1')
        user = authenticate(self.request, username=email, password=password)
        login(self.request, user=user)
        return super().form_valid(form)
