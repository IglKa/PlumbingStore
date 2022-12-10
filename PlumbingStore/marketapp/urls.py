from django.urls import path

from .views import *


app_name = 'marketapp'
urlpatterns = [
    path('', MarketHome.as_view(), name='homepage'),
    # TODO: Refactor
    path('<slug:slug>', AdvertPage.as_view(), name='advert_page'),

    path('company/<slug:slug>/', CompanyDetail.as_view(), name='company'),
    path('company/<slug:slug>/create-advert', CreateAdvert.as_view(), name='create-adv'),
    path('create-company/', CreateCompany.as_view(), name='create-company'),
]
