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
    # TODO: Refactor

    forbidden_symbols = ['@', '.', '/', '$', '#', '*', '+',
                         '?', '%', '>', '<']

    def __init__(self, **kwargs):
        self.kwargs = {**kwargs}
        print(self.kwargs)

        self.sep = '-'
        self.user = None

    def _get_user(self):
        if 'user' in self.kwargs:
            self.user = str(user)
            self.user = self.user[:self.user.find('@')]
            return self.user
        return self.user

    def _get_sep(self):
        if 'sep' in self.kwargs:
            self.sep = sep
        return self.sep

    def _get_text_for_slug(self):
        self.text_list = []
        for i in self.kwargs:
            if isinstance(self.kwargs[i], str):
                self.text_list.append(self.kwargs[i])
        return self.text_list

    def fill_slug(self):
        text = self._get_sep().join(self._get_text_for_slug())
        while ' ' in text:
            text = text.replace(' ', '')
        return text.lower()