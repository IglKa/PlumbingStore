# Menu block for templates
menu_block = [
    'Profile',
    'My Store',
    'Shopping Cart',
    'Settings',
]

# Will fill slug with the given content
# TODO: Refactor
def fill_slug(data):
    slug = []
    for i in data:
        if data[i] == None:
            data[i] = 'None'
        slug.append(data[i])
    return '-'.join(slug)


class AddContextMixin:
    """The Mixin that adds all context needed for the site"""

    def add_context(self, **kwargs):
        context = kwargs
        context['menu'] = menu_block
        return context
