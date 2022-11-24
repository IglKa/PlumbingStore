from django.views import View
from django.views.generic import ListView
from django.views.generic.edit import CreateView
from django.http import HttpResponseRedirect
from django.shortcuts import render, reverse
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Advertisment, Feedback
from .forms import CreateFeedbackForm
from usersapp.models import User

# TODO: РЕФАКТОРИНГ


# TODO: relocate to utils.py
# The <div> where all the links will be displayed
menu_block = [
    'Profile',
    'My Store',
    'Shopping Cart',
    'Settings',
]


class MarketHome(ListView):
    model = Advertisment
    template_name = 'base.html'
    context_object_name = 'advert'

    def get_context_data(self, **kwargs):
        """Adds menu in template"""
        context = super().get_context_data(**kwargs)
        context['menu'] = menu_block
        return context


class CreateAdvert(LoginRequiredMixin, CreateView):
    model = Advertisment
    fields = ['category', 'title',
              'description', 'image'
              ]
    template_name = 'marketapp/createadvert.html'
    success_url = reverse_lazy('marketapp:homepage')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class AdvertPage(View):
    """
    View for the advertisment page. It will render the page with:
    advertisment information;
    feedbacks;
    form to add feedbacks.
    """
    template_name = 'marketapp/advert.html'
    # TODO: Сделать Mixin для поиска объявлений, сделать рефакторинг

    def get(self, request, adv_pk):
        advert = Advertisment.objects.get(pk=adv_pk)
        feedback = Feedback.objects.filter(advert=adv_pk)
        form = CreateFeedbackForm()
        return render(request, self.template_name, {'advert': advert,
                                                    'feedback': feedback,
                                                    'form': form}
                      )

    @method_decorator(login_required)
    def post(self, request, adv_pk):
        form = CreateFeedbackForm(self.request.POST)
        if form.is_valid():
            # Adding user who creates the form to it
            form.instance.user = self.request.user
            # Adding advertisment which feedback belongs to
            form.instance.advert = Advertisment.objects.get(pk=adv_pk)
            form.save()
            # Redirect to the same page
            return HttpResponseRedirect(reverse('marketapp:advert_page', kwargs={'adv_pk': adv_pk}))
