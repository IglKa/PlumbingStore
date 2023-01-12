from django.urls import path
from django.contrib.auth.decorators import login_required

from .views import *

app_name = 'marketapp'
urlpatterns = [
    path('', MarketHome.as_view(), name='homepage'),

    path('<slug:slug>/', AdvertDetailView.as_view(), name='advert-page'),
    # Separate advert page and feedbacks
    path('<slug:slug>/feedbacks', FeedbackSection.as_view(), name='feedback-section'),

    path('company/<slug:slug>/', CompanyDetail.as_view(), name='company'),
    # path('company/<slug:slug>/follow', login_required(FollowCompany.as_view()), name='follow'),
    path('company/<slug:slug>/create-advert', login_required(CreateAdvert.as_view()), name='create-adv'),
   # path('create-company/', CreateCompany.as_view(), name='create-company'),
]
