from django.urls import path

from .views import *


appname = 'shopapp'

urlpatterns = [
    path('<slug:slug>', CompanyDetail.as_view(), name='companys'),
]
