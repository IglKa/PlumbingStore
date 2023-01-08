from django.views.generic import View
from django.shortcuts import render, redirect

from usersapp.forms import UserForm
from usersapp.services import end_registration


class UserCreation(View):
    template_name = 'usersapp/registration.html'
    form_class = UserForm

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {'form': self.form_class})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            end_registration(request, form)
            return redirect('marketapp:homepage')
        return render(request, self.template_name, {'form': self.form_class})
