from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

from . import views


app_name = 'usersapp'

urlpatterns = [
    path('logout/', LogoutView.as_view(), name='logout'),

    path('login/', LoginView.as_view(template_name='usersapp/login.html'), name='login'),
    path('registration/', views.UserCreation.as_view(), name='registration'),

    path('<int:pk>/', views.ProfileView.as_view(), name="profile"),

]
