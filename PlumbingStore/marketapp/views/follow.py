from django.views.generic.edit import CreateView

from marketapp.models import Follow
from marketapp.businesslogic import get_model_instance


class FollowCompany(CreateView):
    """Logic for following company"""

    model = Follow
    template_name = 'marketapp/company.html'

    def form_valid(self, form):
        user = self.request.user
        form.instance.user = user
        form.instance.company = get_model_instance(self.request.POST.get('slug'))
        return super().form_valid(form)
