# Menu block for templates
menu_block = [
    'Profile',
    'My Store',
    'Shopping Cart',
    'Settings',
]


class AddContextMixin:
    """The Mixin that adds all context needed for the site"""

    def add_context(self, **kwargs):
        context = kwargs
        context['menu'] = menu_block
        return context
