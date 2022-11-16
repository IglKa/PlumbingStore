from django.urls import path

from .views import *


app_name = 'marketapp'
urlpatterns = [
    path('', MarketHome.as_view(), name='homepage'),
    path('<int:adv_pk>/', AdvertDetail.as_view(), name='adv_det'),
]
