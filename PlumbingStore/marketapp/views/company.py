from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.detail import SingleObjectMixin
from django.views.generic.edit import CreateView
from django.views.generic import ListView

import utils
from marketapp.forms import CreateAdvertForm
from marketapp.models import Advertisment, Company


class CreateCompany(CreateView):
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
        slug = utils.SlugHandle(user=self.request.user,
                           name=form.instance.name
                            )
        form.instance.slug = slug.fill_slug()
        return super().form_valid(form)


# Same concept as with advert page.
# The only thing I don't like here, that it's actually copying advert page.
class CompanyDetail(SingleObjectMixin, ListView):
    model = Company
    template_name = 'marketapp/company.html'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object(queryset=Company.objects.all())
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['advert'] = self.object
        return context

    def get_queryset(self):
        return self.object.advertisment_set.all()


class CreateAdvert(LoginRequiredMixin, CreateView):
    model = Advertisment
    form_class = CreateAdvertForm
    template_name = 'marketapp/createadvert.html'

    def form_valid(self, form):
        # Assigning company to advert instance
        form.instance.company = Company.objects.get(slug=self.kwargs.get('slug'))
        # Calling slug maker and giving it company slug and title of advert.
        form.instance.slug = utils.SlugHandle(slug_text=[self.kwargs.get('slug'),
                                                         form.instance.title]
                                             )
        return super().form_valid(form)
