from django.views.generic import DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import UserForm
from .models import User
from .businesslogic import end_registration

class ProfileView(LoginRequiredMixin, DetailView):
    """ User Profile Page"""
    model = User
    template_name = 'registration/profile.html'
    context_object_name = 'profile'


class UserCreation(CreateView):
    template_name = 'registration/registration.html'
    form_class = UserForm

    def form_valid(self, form):
        form.save()
        end_registration(self.request)
