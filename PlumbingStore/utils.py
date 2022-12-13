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
    """
    This will be an automatic slug maker.
    As long as I want to build beautiful slugs
    lately I would build my own package for it, but now
    this what I have so far.
    BTW this my first experience on working
    with self-made classes that actually do some work so don't be
    so strict who is watching it :) .
    """

    forbidden_symbols = ['@', '.', '/', '$', '#', '*', '+',
                         '?', '%', '>', '<']

    def __init__(self, **kwargs):
        for key, value in kwargs:
            if value != None or False:
                self.kwargs = self.kwargs | dict(key, value)
                continue
            return self.kwargs

    def _get_user(self):
        if user in self.kwargs:
            self.user = str(user)
            return self.user[:self.user.find('@')]
        return None

    def _get_sep(self):
        if sep in self.kwargs:
            return setattr(self, 'sep', sep)
        return setattr(self, 'sep', '-')

    def _get_upper_method(self):
        if upper in self.kwargs:
            return True
        return False

    def _get_text_for_slug(self):
        text_list = []
        for i in self.kwargs:
            if isinstance(i, str):
                text_list.append(i)
            else:
                pass

    def fill_slug(self):
        pass
