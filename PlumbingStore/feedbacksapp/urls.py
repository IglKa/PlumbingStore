from django.urls import path

from .views import FeedbackSection


app_name = 'feedbacksapp'

urlpatterns = [
    path('<slug:slug>', FeedbackSection.as_view(), name='feedback-section')
]