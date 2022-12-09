from django.utils import timezone


# Menu block for templates
menu_block = [
    # Userapp logic
    {'title': 'login', 'url_name': 'login'},
    {'title': 'logout', 'url_name': 'logout'},
    {'title': 'register', 'url_name': 'registration'},
    # Other logic
    {'title': 'Settings', 'url_name': 'settings'},
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

    # I will think on translatoins later, now my site is English only.
    def __init__(
                 self,
                 user=None,
                 title=None,
                 category=None,
                 description=None,
                 capitalize=False,
                 upper=False,
                 lower=True,
                 sep='-',
                 ):

        self.user = user
        self.title = title
        self.description = description
        self.category = category
        self.capitalize = capitalize
        self.upper = upper
        self.lower = lower
        self.sep = sep


    def _normalize_user(self):
        # Checking if user is str type
        if isinstance(self.user, str) == False:
            self.user = str(self.user)
        self.user = self.user
        # Because I want my site to use email instead of usernames
        # we need to find '@' symbol and remove @email.com
        self.user = self.user[:self.user.find('@')]
        return self.user

    def _normalize_title(self):
        # Removing all spaces from title
        while ' ' in self.title:
            self.title = self.title.replace(' ', '')
        return self.title

    def fill_slug(self):
        # Need to write checks for attributes if they are given or not.
        # But now I don't really know how to do this
        return self._normalize_user() + self.sep + self._normalize_title()
