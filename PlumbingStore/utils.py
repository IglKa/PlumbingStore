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

    def __init__(self, **kwargs):
        # TODO: Рассписать все возможные атрибуты
        self.user = str(kwargs['user'])
        self.user = self.user[:self.user.find('@')]
        self.title = kwargs['title'].capitalize().strip().replace(' ', '')

    # TODO: def normalize_<self.<value>>(self, **kwargs):
    #  will do all work like: translate ru-eng, strip, remove no_no_symbols

    def fill_slug(self):
        slug = self.user + '-' + self.title
        return slug


class AddContextMixin:
    """The Mixin that adds all context needed for the site"""

    def add_context(self, **kwargs):
        context = kwargs
        context['menu'] = menu_block
        return context
