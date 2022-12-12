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


# TODO: rethink what to do with that and rid off of this tinki-winki ass-shit
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
        self.kwargs = {}
        for key, value in kwargs:
            self.kwargs = self.kwargs | dict(key, value)

        self.sep = getattr(self, 'sep', default='-')
        self.low = getattr(self, 'low', default=True)
        self.upp = getattr(self, 'upp', default=False)
        # If user is given setting it as attr
        if user in kwargs:
            setattr(self, 'user', user)
        else:
            pass

    def _normalize_user(self):
        # Checking if user is str type
        if isinstance(self.user, str) == False:
            self.user = str(self.user)
        self.user = self.user
        # Because I want my site to use email instead of usernames
        # we need to find '@' symbol and remove @email.com
        self.user = self.user[:self.user.find('@')]
        return self.user

    def fill_slug(self):
        # Need to write checks for attributes if they are given or not.
        # But now I don't really know how to do this
        return self._normalize_user() + self.sep + self._normalize_title()
