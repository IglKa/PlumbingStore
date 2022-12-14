from django.utils import timezone


# Menu block for templates
# TODO: Think better on functional that menu block will provide
menu_block = [
    # Settings
    # {'title': 'Settings', 'url_name': 'settingsapp:mainmenu'},
]


class AddContextMixin:
    """The Mixin that adds all context needed for the site"""

    def add_context(self, **kwargs):
        context = kwargs
        context['menu'] = menu_block
        return context


class SlugHandle:
    """ Auto Slug Maker """

    # TODO: Refactor; think on making it as CustomField.
    forbidden_symbols = ['@', '.', '/', '$', '#', '*', '+',
                         '?', '%', '>', '<']

    def __init__(self, slug_text: list, **kwargs):
        # Necessary attribute that will be forming text for slug
        self.slug_text = slug_text
        for key, value in kwargs:
            setattr(self, str(key), value)

    # I would like to do something that will search given attributes for:
    # 'lower', 'upper' or 'capitalize'
    # to lately use it in forming slug. But I don't really know how to do this.

    def _methods_check(self):
        pass

    def _get_sep(self):
        self.sep = getattr(self, 'sep', default='-')
        return self.sep

    def _slug_text(self):
        self.slug_text = self.sep.join(self.slug_text)
        return self.slug_text