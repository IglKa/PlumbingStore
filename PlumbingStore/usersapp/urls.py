from django.urls import path, include

from . import views


app_name = 'usersapp'

urlpatterns = [
    path('', include('django.contrib.auth.urls')),

    path('registration/', views.UserCreation.as_view(), name='registration'),
    path('<int:pk>/', views.ProfileView.as_view(), name="profile"),

]
