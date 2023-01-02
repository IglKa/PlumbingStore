from django.urls import path

from . import views


app_name = 'usersapp'

urlpatterns = [
    path('login/', views.UserLogin.as_view(), name='login'),
    path('registration/', views.UserCreation.as_view(), name='registration'),

    path('<int:pk>/', views.ProfileView.as_view(), name="profile"),

]
