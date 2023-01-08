from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

from .views import *


app_name = 'usersapp'

urlpatterns = [
    path('logout/', LogoutView.as_view(), name='logout'),

    path('login/', LoginView.as_view(template_name='usersapp/login.html'), name='login'),
    path('registration/', UserCreation.as_view(), name='registration'),

    path('<int:pk>/', ProfileView.as_view(), name="profile"),

]
