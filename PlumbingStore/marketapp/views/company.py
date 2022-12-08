from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.views.generic import DetailView

from marketapp.models import Advertisment
from marketapp.models import Company
import utils


class CreateCompany(CreateView):
    model = Company
    template_name = 'marketapp/createcompany.html'
    fields = ['category',
              'name', 'descr',
              'header_image', 'profile_image',
              ]
    success_url = ''

    def form_valid(self, form):
        form.instance.user = self.request.user
        slug = utils.SlugHandle(user=self.request.user,
                           title=form.instance.name
                           # Now I am actually hate myself for not ending it up
                            )
        form.instance.slug = slug.fill_slug()
        return super().form_valid(form)


class CompanyDetail(DetailView):
    model = Company
    template_name = 'marketapp/company.html'
    context_object_name = 'company'

# TODO: merge
class CreateAdvert(LoginRequiredMixin, CreateView):
    model = Advertisment
    fields = ['category', 'title',
              'description', 'image'
              ]
    template_name = 'marketapp/createadvert.html'
    success_url = reverse_lazy('marketapp:homepage')

    def form_valid(self, form):
        # Adds User to Advertisment
        form.instance.user = self.request.user
        form.save(commit=False)
        slug = utils.SlugHandle(user=self.request.user, title=form.instance.title)
        form.instance.slug = slug.fill_slug()
        return super().form_valid(form)
