from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.views import View
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin

from marketapp.models import Advertisment, Feedback, Company
from marketapp.forms import CreateFeedbackForm


class AdvertPage(LoginRequiredMixin, View):


    template_name = 'marketapp/advert.html'

    def get(self, request, slug):
        advert = get_object_or_404(Advertisment, slug=slug)
        feedback = Feedback.objects.filter(advert=advert)
        return render(request, self.template_name, {'advert': advert,
                                                    'feedback': feedback,
                                                    'form': CreateFeedbackForm()}
                      )

    def post(self, request, slug):
        form = CreateFeedbackForm(self.request.POST)
        if form.is_valid():
            # Adding user who creates the form
            form.instance.user = self.request.user
            # Adding advertisment which feedback belongs to
            form.instance.advert = Advertisment.objects.get(slug=slug)
            form.save()
            # Redirect to the same page
            return HttpResponseRedirect(reverse('marketapp:advert_page',
                                                kwargs={'slug': slug}
                                                )
                                        )
