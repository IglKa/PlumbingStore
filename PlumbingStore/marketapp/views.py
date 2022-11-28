from django.views import View
from django.views.generic import ListView
from django.views.generic.edit import CreateView
from django.http import HttpResponseRedirect
from django.shortcuts import render, reverse, get_object_or_404
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Advertisment, Feedback
from .forms import CreateFeedbackForm
from utils import AddContextMixin, SlugHandle
# TODO: РЕФАКТОРИНГ


class MarketHome(AddContextMixin, ListView):
    """Main Home Page"""
    model = Advertisment
    template_name = 'base.html'
    context_object_name = 'advert'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        # Adding context from Mixin
        addable_context = self.add_context()
        return dict(list(context.items()) + list(addable_context.items()))


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
        slug = SlugHandle(form)
        slug = slug.fill_slug()
        form.instance.slug = slug
        return super().form_valid(form)


class AdvertPage(View):
    """
    View for the advertisment page. It will render the page with:
    advertisment information;
    feedbacks;
    form to add feedbacks.
    """
    template_name = 'marketapp/advert.html'

    def get(self, request, adv_slug):
        advert = get_object_or_404(Advertisment, slug=adv_slug)
        feedback = Feedback.objects.filter(advert=advert)
        form = CreateFeedbackForm()
        return render(request, self.template_name, {'advert': advert,
                                                    'feedback': feedback,
                                                    'form': form}
                      )

    @method_decorator(login_required)
    def post(self, request, adv_slug):
        form = CreateFeedbackForm(self.request.POST)
        if form.is_valid():
            # Adding user who creates the form
            form.instance.user = self.request.user
            # Adding advertisment which feedback belongs to
            form.instance.advert = Advertisment.objects.get(slug=adv_slug)
            form.save()
            # Redirect to the same page
            return HttpResponseRedirect(reverse('marketapp:advert_page',
                                                kwargs={'adv_slug': adv_slug}
                                                )
                                        )
