from django.contrib.auth import login, authenticate
from django.views.generic import TemplateView, DetailView
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

from django.shortcuts import redirect

from .forms import UserForm
from .models import User
# TODO: Исправить баг со входом


# User profile page
class ProfileView(LoginRequiredMixin, DetailView):
    model = User
    template_name = 'registration/profile.html'
    context_object_name = 'profile'


# TODO: Убрать временную пагу и добавить нормальную страницу
class TemplateView(TemplateView):
    template_name = 'registration/page.html'


# Только сейчас понял отличия CreateView от FormView.
# FormView - отображает форму, проверяет её валидность и редиректит на success_url при успехе.
# CreateView - отображает форму, проверяет валидность, ДОБАВЛЯЕТ ФОРМУ В БД и редиректит при успехе.
class UserCreation(CreateView):
    template_name = 'registration/registration.html'
    form_class = UserForm
    success_url = '/'

    def form_valid(self, form):
        form.save()
        email = self.request.POST['email']
        password = self.request.POST['password']
        user = authenticate(self.request, username=email, password=password)
        login(self.request, user=user)
        return redirect(self.success_url)
