from django.views.generic import ListView

import utils
from mainapp.models import Advertisment


class MarketHome(ListView):
    """Main Home Page"""

    model = Advertisment
    template_name = 'base.html'
    context_object_name = 'advert'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        # Adding context from Mixin
        addable_context = utils.add_context()
        return dict(list(context.items()) + list(addable_context.items()))
