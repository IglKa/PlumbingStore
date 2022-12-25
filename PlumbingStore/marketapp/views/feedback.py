from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, View
from django.views.generic.detail import SingleObjectMixin

from marketapp.models import Advertisment, Feedback
from marketapp.forms import CreateFeedbackForm
from utils import AddContextMixin


class FeedbackContextView(AddContextMixin, SingleObjectMixin, ListView):
    """
    Feedback Context View.

    This will be providing context for feedback section page.
    """

    template_name = 'marketapp/feedback-section.html'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object(queryset=Advertisment.objects.all())
        return super().get(request, *args, **kwargs)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        # Because of little problem that separating Advertisment and Feedbacks
        # cause, we need to give slug of advert to template(it's lately used on page title and form).
        context['advert_slug'] = self.object.slug
        context['menu'] = self.add_context()
        context['form'] = CreateFeedbackForm()
        return context

    def get_queryset(self):
        return self.object.feedback_set.all()


class SendFeedbackView(LoginRequiredMixin, CreateView):
    """
    Feedback form handle.

    This one is providing logic for post request on feedback section page.
    """

    form_class = CreateFeedbackForm
    template_name = 'marketapp/feedback-section.html'

    def form_valid(self, form, *args, **kwargs):
        form.instance.user = self.request.user
        form.instance.advert = Advertisment.objects.get(slug=self.kwargs.get('slug'))
        return super().form_valid(form)


class FeedbackSectionView(View):
    """Feedback section page"""

    # Combining context and logic
    def get(self, request, *args, **kwargs):
        view = FeedbackContextView.as_view()
        return view(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        view = SendFeedbackView.as_view()
        return view(request, *args, **kwargs)
