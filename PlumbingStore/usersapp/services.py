from django.contrib.auth import authenticate, login


def end_registration(request, form):
    email = request.POST.get('email')
    password = request.POST.get('password')
    user = authenticate(username=email, password=password)
    login(request, user=user)