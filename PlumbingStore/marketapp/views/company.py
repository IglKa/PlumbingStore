from django.views.generic.edit import CreateView
from django.views.generic import DetailView

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
