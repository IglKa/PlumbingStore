from django.views.generic.edit import CreateView

import utils
from marketapp.forms import CreateAdvertForm
from marketapp.models import Advertisment, Company


class CreateAdvert(CreateView):
    """Create Advertisment View"""

    model = Advertisment
    form_class = CreateAdvertForm
    template_name = 'marketapp/createadvert.html'

    def form_valid(self, form):
        # Assigning company to advert instance
        form.instance.company = Company.objects.get(slug=self.kwargs.get('slug'))
        # Calling slug maker and giving it company slug and title of advert.
        slug = utils.SlugHandle(slug_text=[self.kwargs.get('slug'),
                                           form.instance.title
                                           ]
                                )
        form.instance.slug = slug.form_slug_text()
        return super().form_valid(form)