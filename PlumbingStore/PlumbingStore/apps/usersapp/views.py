from django.contrib.auth import login, authenticate
from django.views.generic import TemplateView, DetailView
from django.views.generic.edit import FormView

from .forms import UserForm
from .models import User


# User profile page
class ProfileView(DetailView):
    model = User
    template_name = 'registration/profile.html'
    context_object_name = 'profile'


# TODO: Убрать временную пагу и добавить нормальную страницу
class TemplateView(TemplateView):
    template_name = 'registration/page.html'


class UserCreation(FormView):
    template_name = 'registration/registration.html'
    form_class = UserForm
    success_url = '/'

    def form_valid(self, form):
        form.save()
        email = self.request.POST['email']
        password = self.request.POST['password']
        user = authenticate(self.request, username=email, password=password)
        login(self.request, user=user)
        return super().form_valid(form)
