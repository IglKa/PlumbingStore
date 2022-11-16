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

    #TODO: Научиться распаковывать dict объекты, поменять "self.request.POST['user']" на id User
    #Тут надо прооперировать словарём. функция принимает его, оперирует и возвращает. Сам request неизменяем.
    def post(self, request):
        user = User.objects.filter(email = self.request.user)[0].id
        self.request.POST['user'] = user
