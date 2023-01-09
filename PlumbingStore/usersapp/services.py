from django.contrib.auth import authenticate, login

from .models import Profile


def end_registration(request, form):
    """Ends the registration process"""

    # TODO: add email confirmation
    email = form.cleaned_data.get('email')
    password = form.cleaned_data.get('password1')
    user = authenticate(request, username=email, password=password)
    login(request, user)


def get_user_profile(request):
    user_profile = Profile.objects.get(user=request.user)
    return user_profile
