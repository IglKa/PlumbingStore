from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.detail import SingleObjectMixin
from django.views.generic.edit import CreateView
from django.views.generic import ListView

import utils
from marketapp.forms import CreateAdvertForm
from marketapp.models import Advertisment, Company


class CreateCompany(CreateView):
    """Creating company logic"""

    # TODO: Think better on how this process will be going, what user needs to input for it, what data to store.
    model = Company
    template_name = 'marketapp/createcompany.html'
    fields = [
        'category',
        'name', 'descr',
        'header_image',
        'profile_image',
              ]

    def form_valid(self, form):
        form.instance.user = self.request.user
        slug = utils.SlugHandle(slug_text=[form.instance.name])
        form.instance.slug = slug.form_slug_text()
        return super().form_valid(form)


# Same concept as with advert page.
# The only thing I don't like here, that it's actually copying advert page.
class CompanyDetail(SingleObjectMixin, ListView):
    """Company Page"""

    model = Company
    template_name = 'marketapp/company.html'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object(queryset=Company.objects.filter(slug=kwargs.get('slug')
                                                                      )
                                      )
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['company'] = self.object
        return context

    def get_queryset(self):
        return self.object.advertisment_set.all()


class CreateAdvert(LoginRequiredMixin, CreateView):
    """Create Advertisment View"""

    model = Advertisment
    form_class = CreateAdvertForm
    template_name = 'marketapp/createadvert.html'

    def form_valid(self, form):
        # Assigning company to advert instance
        form.instance.company = Company.objects.get(slug=self.kwargs.get('slug'))
        # Calling slug maker and giving it company slug and title of advert.
        slug = utils.SlugHandle(slug_text=[self.kwargs.get('slug'),
                                                         form.instance.title]
                                             )
        form.instance.slug = slug.form_slug_text()
        return super().form_valid(form)
