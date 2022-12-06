from django.views import View
from django.views.generic.edit import CreateView
from django.http import HttpResponseRedirect
from django.shortcuts import render, reverse, get_object_or_404
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import LoginRequiredMixin

from marketapp.models import Advertisment, Feedback, Company
from marketapp.forms import CreateFeedbackForm
import utils


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


# TODO: Refactor - class AdvertPage(SingleObjectMixin, DetailView)
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
