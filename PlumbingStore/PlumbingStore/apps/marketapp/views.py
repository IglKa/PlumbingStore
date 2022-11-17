from usersapp.models import User
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView

from .models import Advertisment, Feedback
from .forms import CreateAdvert


class MarketHome(ListView):
    model = Advertisment
    template_name = 'marketapp/markethome.html'
    context_object_name = 'advert'


class AdvertDetail(DetailView):
    model = Advertisment
    template_name = 'marketapp/advert.html'
    context_object_name = 'advert'
    #TODO: Сделать поиск по slug
    pk_url_kwarg = 'adv_pk'


class CreateAdvert(CreateView):
    form_class = CreateAdvert
    template_name = 'marketapp/createadvert.html'
    context_object_name = 'advert'


    def post(self, request):
        #Because I don't want to give QueryDict 'user' field right from the form, I override the
        #post method here.
        user = User.objects.filter(email=self.request.user)[0].id
        context = self.request.POST.copy()
        context['user'] = user
        return context
