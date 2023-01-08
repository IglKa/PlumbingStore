from django.views.generic import DetailView, View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

from .models import User
from .forms import UserForm
# from .services import end_registration


class ProfileView(LoginRequiredMixin, DetailView):
    """ User Profile Page"""

    model = User
    template_name = 'usersapp/profile.html'
    context_object_name = 'profile'


class UserCreation(View):
    template_name = 'usersapp/registration.html'
    form_class = UserForm

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {'form': self.form_class})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password1')
            user = authenticate(request, username=email, password=password)
            login(request, user)
            return redirect('marketapp:homepage')
        return render(request, self.template_name, {'form': self.form_class})