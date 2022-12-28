from django.utils import timezone
from django.db import models


# Menu block for templates
# TODO: Think better on functional that menu block will provide
menu_block = [
    # Settings
    # {'title': 'Settings', 'url_name': 'settingsapp:mainmenu'},
]

def get_object_rating(object):
    ratings = Feedback.objects.filter(content_object=object).values_list('rating', flat=True)
    return round(sum(ratings) / len(ratings), 1)

class AddContextMixin:
    """The Mixin that adds all context needed for the site"""

    def add_context(self, **kwargs):
        context = kwargs
        context['menu'] = menu_block
        return context


class SlugHandle:
    """ Auto Slug Maker """

    # TODO: Refactor; think on making it as CustomField.
    forbidden_symbols = ['/', '%', '>', '<',
                         '"', '\\', '№', '`',
                         '^', '{', '}']

    def __init__(self, slug_text: list, **kwargs):
        # Necessary attribute that will be forming text for slug
        self.slug_text = slug_text
        for key in kwargs:
            setattr(self, key, kwargs[key])

    def form_slug_text(self):
        sep = getattr(self, 'sep', '-')
        text = sep.join(self.slug_text)
        while ' ' in text:
            text = text.replace(' ', '')
        return self._forbidden_symbols(text)

    def _forbidden_symbols(self, text):
        for i in self.forbidden_symbols:
            if i in text:
                text = text.replace(i, '')
        return text

    # I would like to do something that will search given attributes
    # for method to use in forming slug.
    # like 'lower', 'upper' or 'capitalize'
    # But I don't really know how to do this.

    def _methods_check(self):
        pass
