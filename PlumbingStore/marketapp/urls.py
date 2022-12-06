from django.urls import path

from .views import *


app_name = 'marketapp'
urlpatterns = [
    path('', MarketHome.as_view(), name='homepage'),

    path('<slug:adv_slug>', AdvertPage.as_view(), name='advert_page'),
    path('create-advert/', CreateAdvert.as_view(), name='create_adv'),

    path('company/<slug:slug>', CompanyDetail.as_view(), name='company'),
    path('create-company/', CreateCompany.as_view(), name='create-company'),
]
