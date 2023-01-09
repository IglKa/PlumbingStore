from django.contrib.auth.mixins import LoginRequiredMixin # TODO: Permission required
from django.views.generic import CreateView

from marketapp.forms import CreateAdvertForm
from marketapp.models import Advertisment
from marketapp.services import get_model_instance
from utils import SlugHandle


class CreateAdvert(LoginRequiredMixin, CreateView):
    """Create Advertisment View"""

    model = Advertisment
    form_class = CreateAdvertForm
    template_name = 'marketapp/createadvert.html'

    def form_valid(self, form):
        # Assigning company to advert instance
        form.instance.company = get_model_instance(slug=self.kwargs.get('slug'))
        # Calling slug maker and giving it company slug and title of advert.
        slug = SlugHandle(slug_text=[self.kwargs.get('slug'),
                                           form.instance.title
                                           ]
                                )
        form.instance.slug = slug.form_slug_text()
        return super().form_valid(form)
