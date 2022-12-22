from django.views.generic.edit import CreateView
from django.views.generic.detail import SingleObjectMixin

from marketapp.models import Rating, Advertisment

class AddRatingView(SingleObjectMixin, CreateView):
    model = Advertisment
    success_url = 'marketapp:advert-page'
