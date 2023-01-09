from django.views.generic.edit import CreateView

from marketapp.models import Follow
from marketapp.services import set_follow
from marketapp.forms import FollowForm


class FollowCompany(CreateView):
    """Logic for following company"""

    model = Follow
    template_name = 'marketapp/company.html'
    form_class = FollowForm

    def form_valid(self, form):
        set_follow(self.request, form)
        return super().form_valid(form)
