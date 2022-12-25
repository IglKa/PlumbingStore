from django.views.generic import ListView

from marketapp.models import Advertisment
import utils


class MarketHome(utils.AddContextMixin, ListView):
    """Main Home Page"""

    model = Advertisment
    template_name = 'base.html'
    context_object_name = 'advert'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        # Adding context from Mixin
        addable_context = self.add_context()
        return dict(list(context.items()) + list(addable_context.items()))
