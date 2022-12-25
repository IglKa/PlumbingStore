from django.views.generic import DetailView

from marketapp.models import Advertisment, Feedback, Company
from utils import AddContextMixin


# I had separated Advertisment page and Feedback section for
# optimization of QuerySets that was going to DB.
class AdvertDetailView(AddContextMixin, DetailView):
    """Advertisment detail"""

    model = Advertisment
    template_name = 'marketapp/advert.html'
    context_object_name = 'advert' # Isn't working don't know why.

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = self.add_context()
        return context

# Might provide some logic here, but for now leaving it till later.