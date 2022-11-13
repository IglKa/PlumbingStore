from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    context = 'Hello, User!'
    return render(request, 'usersapp/registration.html', {'context': context})
