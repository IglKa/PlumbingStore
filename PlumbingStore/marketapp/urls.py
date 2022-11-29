from django.urls import path

from .views import *


app_name = 'marketapp'
urlpatterns = [
    path('', MarketHome.as_view(), name='homepage'),

    path('<slug:adv_slug>', AdvertPage.as_view(), name='advert_page'),

    path('create/', CreateAdvert.as_view(), name='create_adv')
]