from django.urls import path, include

from . import views


app_name = 'usersapp'

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('registration/', views.index, name='registration')
]
