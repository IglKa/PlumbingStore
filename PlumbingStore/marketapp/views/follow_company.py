from django.views.generic.edit import CreateView
from django.urls import reverse

from .company_detail import CompanyDetail
from marketapp.services import set_follow
from marketapp.forms import FollowForm


class FollowCompany(CreateView):
    """Logic for following company"""

    template_name = 'marketapp/company.html'
    form_class = FollowForm

    def get(self, request, *args, **kwargs):
        view = CompanyDetail.as_view()
        return view(request, *args, **kwargs)

    def form_valid(self, form):
        self.form = set_follow(self.request, form)
        return super().form_valid(self.form)

    def get_success_url(self):
        return reverse('marketapp:company', kwargs={'slug': self.request.POST.get('slug')})
