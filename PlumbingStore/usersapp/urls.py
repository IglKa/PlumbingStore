from django.urls import path, include

from . import views


app_name = 'usersapp'

urlpatterns = [
    path('logout/', views.UserLogout.as_view(), name='logout'),

    path('login/', views.UserLogin.as_view(), name='login'),
    path('registration/', views.UserCreation.as_view(), name='registration'),

    path('<int:pk>/', views.ProfileView.as_view(), name="profile"),

]
