from typing import Union

from django.db.models import QuerySet
from django.http import Http404

from .models import Advertisment, Company
import usersapp.services as user_serv


# TODO: Provide logic for Follow
def update_rating(model_instance):
    """Update rating for either Advertisment or Company"""

    ratings = find_feedbacks(model_instance).values_list('rating', flat=True)
    model_instance.rating = round(sum(ratings) / len(ratings), 1)
    model_instance.save()


def find_feedbacks(model_instance) -> QuerySet:
    """Find feedbacks for given object"""

    feedbacks = model_instance.feedbacks.all()
    return feedbacks


def get_model_instance(slug: str) -> Union[Advertisment, Company]:
    """
    I think that this view will be something like 'generic'.
    It would find either Advertisment or Company (based on the given slug).
    """

    #TODO: Lately try to re-do this cuz it looks assly ugly.
    models_to_search = [Advertisment, Company]
    for Object in models_to_search:
        try:
            model_instance = Object.objects.get(slug=slug)
        except:
            continue
        else:
            return model_instance
    raise Http404


def set_follow(request, form) -> None:
    """Ends follow request"""
    form.instance.profile = user_serv.get_user_profile(request)
    form.instance.company = get_model_instance(request.POST.get('slug'))
