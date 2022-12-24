from django.views.generic.edit import CreateView
from django.views.generic.detail import SingleObjectMixin

from marketapp.models import Advertisment


#class AddRatingView(CreateView):
   # model = Rating
   ## success_url = 'marketapp:advert-page'
    #template_name = 'marketapp/advert.html'
    #form_class = RatingForm

   # def form_valid(self, form, **kwargs):
      #  self.object = Advertisment.objects.get(self.kwargs.get('slug'))
      #  form.instance.advert = self.object
       ## form.instance.star = self.kwargs.get('star')
      #  return super().form_valid(form)
        