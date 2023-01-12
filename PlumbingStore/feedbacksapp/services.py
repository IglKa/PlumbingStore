from typing import Union

from django.db.models import QuerySet
from django.http import Http404

from mainapp.models import Advertisment, Company
from utils import add_context


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


def get_feedback_section_context(slug, form, ):
    context = {
        'object_slug': slug,
        'form': form,
        'feedbacks': find_feedbacks(get_model_instance(slug)),
        'menu': add_context()
    }
    return context


def create_feedback_instance(user, form, model_instance):
    form.instance.user = user
    form.instance.content_object = model_instance
    form.save()


def end_feedback_post_logic(user, form, model_instance):
    create_feedback_instance(user, form, model_instance)
    update_rating(model_instance)