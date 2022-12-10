from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views import View
from django.views.generic.edit import CreateView
from django.views.generic import DetailView

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
    success_url = ''

    def form_valid(self, form):
        form.instance.user = self.request.user
        slug = utils.SlugHandle(user=self.request.user,
                           title=form.instance.name
                           # Now I am actually hate myself for not ending it up
                            )
        form.instance.slug = slug.fill_slug()
        return super().form_valid(form)


# Same concept as with advert page.
# The only thing I don't like here, that it's actually copying advert page.
class CompanyDetail(DetailView):
    model = Company
    template_name = 'marketapp/company.html'
    context_object_name = 'company'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = CreateAdvertForm()
        return context


class CreateAdvert(LoginRequiredMixin, CreateView):
    model = Advertisment
    form_class = CreateAdvertForm
    template_name = 'marketapp/createadvert.html'
    success_url = reverse_lazy('marketapp:homepage')

    def form_valid(self, form):
        # Adds User to Advertisment
        form.instance.user = self.request.user
        form.save(commit=False)
        slug = utils.SlugHandle(user=self.request.user, title=form.instance.title)
        form.instance.slug = slug.fill_slug()
        return super().form_valid(form)


class CompanyPageView(View):
    def get(self, request, *args, **kwargs):
        view = CompanyDetail.as_view()
        return view(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        view = CreateAdvert.as_view()
        return view(request, *args, **kwargs)