from django.views.generic import ListView
from django.views.generic.detail import SingleObjectMixin

from marketapp.models import Advertisment, Company


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



