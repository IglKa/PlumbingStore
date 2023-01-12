from typing import Union

from django.db.models import QuerySet
from django.http import Http404

from mainapp.models import Advertisment, Company
from utils import add_context
from usersapp.services import get_user_profile


def get_feedback_section_context(slug, form) -> dict:
    context = {
        'object_slug': slug,
        'form': form,
        'feedbacks': find_feedbacks(get_model_instance(slug)),
        'menu': add_context()
    }
    return context


def end_feedback_post_logic(user, form, model_instance) -> None:
    create_feedback_instance(user, form, model_instance)
    update_rating(model_instance)


def create_feedback_instance(user, form, model_instance) -> None:
    """Will find user profile and create feedbacks instance"""
    form.instance.profile = get_user_profile(user)
    form.instance.content_object = model_instance
    form.save()


def update_rating(model_instance) -> None:
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
