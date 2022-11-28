from django.utils import timezone


# Menu block for templates
menu_block = [
    'Profile',
    'My Store',
    'Shopping Cart',
    'Settings',
]


class SlugHandle:
    """This will be an automatic slug maker.
    As long as I want to build beautiful slugs
    lately I would build my own package for it, but now
    this what I have so  far. BTW this my first experience on working
    with self-made classes that actually do some work.
    """
    no_no_symbols = ['@', '.', '/', '$', '#', '*', '+',
                     '?', '%', '>', '<']

    def __init__(self, form, **kwargs):
        self.user = str(form.instance.user).translate({ord(i): None for i in self.no_no_symbols})
        self.title = form.instance.title

    def fill_slug(self):
        slug = self.user + '-' + self.title
        return slug.strip()


class AddContextMixin:
    """The Mixin that adds all context needed for the site"""

    def add_context(self, **kwargs):
        context = kwargs
        context['menu'] = menu_block
        return context
