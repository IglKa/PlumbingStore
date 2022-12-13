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
    # TODO: Refactor

    # I have build something by myself. Feels cool. But I know that this is a goofy af code.
    # I need to actually refactor it to get more beautiful code. It need's a lot of work on it, sadly or luckly.

    forbidden_symbols = ['@', '.', '/', '$', '#', '*', '+',
                         '?', '%', '>', '<']

    def __init__(self, **kwargs):
        self.kwargs = {**kwargs}

        self.sep = '-'
        self.user = None

    def _get_user(self):
        if 'user' in self.kwargs:
            self.user = str(user)
            self.user = self.user[:self.user.find('@')]
            return self.user
        return self.user
    # I don't know about this two methods, but I will probably delete it later.
    def _get_sep(self):
        if 'sep' in self.kwargs:
            self.sep = sep
        return self.sep

    def _get_text_for_slug(self):
        # Giving a list of values that are str type and will be a future slug.
        self.text_list = []
        for i in self.kwargs:
            if isinstance(self.kwargs[i], str):
                self.text_list.append(self.kwargs[i])
        return self.text_list

    def fill_slug(self):
        # With given separator join self.text_list
        text = self._get_sep().join(self._get_text_for_slug())
        # While spaces are in text we need to delete it.
        while ' ' in text:
            text = text.replace(' ', '')
        return text.lower()