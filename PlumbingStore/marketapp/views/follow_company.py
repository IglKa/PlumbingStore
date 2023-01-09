from django.views.generic.edit import CreateView
from django.urls import reverse

from marketapp.models import Follow
from marketapp.services import get_model_instance
from marketapp.forms import FollowForm
import usersapp.services as user_serv


class FollowCompany(CreateView):
    """Logic for following company"""

    model = Follow
    template_name = 'marketapp/company.html'
    form_class = FollowForm

    def form_valid(self, form):
        # set_follow(self.request, form)
        form.instance.company = get_model_instance(self.request.POST.get('slug'))
        form.instance.profile = user_serv.get_user_profile(self.request)
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('marketapp:company', kwargs={'slug': self.request.POST.get('slug')})
