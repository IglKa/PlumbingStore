from django.urls import path
from django.contrib.auth.decorators import login_required

from .views import *

app_name = 'mainapp'
urlpatterns = [
    path('', MarketHome.as_view(), name='homepage'),

    path('<slug:slug>/', AdvertDetailView.as_view(), name='advert-page'),
    # Separate advert page and feedbacks
    path('<slug:slug>/feedbacks', FeedbackSection.as_view(), name='feedback-section'),

    path('<slug:slug>/create-advert', login_required(CreateAdvert.as_view()), name='create-adv'),
]
