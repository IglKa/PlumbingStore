from django.test import TestCase

from PlumbingStore.utils import SlugHandle


slug = SlugHandle(slug_text=[
    'FUCK !THIS@ BUG',
    'YEEEEEEAAAAAAA'
], sep='_')
print(slug.form_slug_text())
