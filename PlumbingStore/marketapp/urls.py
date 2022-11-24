from django.urls import path

from .views import *


app_name = 'marketapp'
urlpatterns = [
    path('', MarketHome.as_view(), name='homepage'),

    path('<int:adv_pk>', AdvertPage.as_view(), name='advert_page'),
    # path('<int:adv_pk>/', AdvertDetail.as_view(), name='adv_det'),
    # path('<int:adv_pk>/create', CreateFeedback.as_view(), name='feedback_create'),

    path('create/', CreateAdvert.as_view(), name='create_adv')
]
