from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView

from usersapp.models import Profile


class ProfileView(LoginRequiredMixin, DetailView):
    """ User Profile Page"""

    model = Profile
    template_name = 'usersapp/profile.html'
    context_object_name = 'profile'
