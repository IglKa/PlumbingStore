from django.contrib.auth import authenticate, login
from django.shortcuts import redirect


def end_registration(request):
    email = request.POST['email']
    password = request.POST['password']
    user = authenticate(request, username=email, password=password)
    login(request, user=user)
    return redirect('marketapp:homepage')