from django.utils import timezone


# Menu block for templates
menu_block = [
    'Profile',
    'My Store',
    'Shopping Cart',
    'Settings',
]


class SlugHandle:
    """
    This will be an automatic slug maker.
    As long as I want to build beautiful slugs
    lately I would build my own package for it, but now
    this what I have so  far. BTW this my first experience on working
    with self-made classes that actually do some work.
    """
    no_no_symbols = ['@', '.', '/', '$', '#', '*', '+',
                     '?', '%', '>', '<']

    # I will think on translatoins later, now my site is English only.
    def __init__(self,
                 user=None,
                 title=None,
                 category=None,
                 description=None,
                 capitalize=False,
                 upper=False,
                 lower=True,
                 sep='-',
                 ):

        # Checking if user is not str type and converting it, if it is
        if isinstance(user, str) == False:
            self.user = str(user)
        else:
            self.user = user

        self.title = title
        self.description = description
        self.category = category
        self.capitalize = capitalize
        self.upper = upper
        self.lower = lower
        self.sep = sep

    # TODO: def normalize_<self.<value>>(self, **kwargs):
    #  will do all work like: translate ru-eng, strip, remove no_no_symbols

    # def fill_slug(self):
        # slug = self.user + '-' + self.title
        # return slug

    def _normalize_user(self):
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
        pass

class AddContextMixin:
    """The Mixin that adds all context needed for the site"""

    def add_context(self, **kwargs):
        context = kwargs
        context['menu'] = menu_block
        return context
