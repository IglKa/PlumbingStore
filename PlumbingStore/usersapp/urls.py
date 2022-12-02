from django.urls import path, include

from . import views


app_name = 'usersapp'

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('page/', views.TemplateView.as_view(), name="page"),

    path('registration/', views.UserCreation.as_view(), name='registration'),
    path('profile/<int:pk>/', views.ProfileView.as_view(), name="profile"),

    path('profile/<int:pk>/adverts/', views.UserAdvertsView.as_view(), name="user_adverts"),
]
