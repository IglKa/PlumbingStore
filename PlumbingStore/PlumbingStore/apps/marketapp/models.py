from django.db import models
from django.utils import timezone


class Advertisment(models.Model):

    class Category(models.TextChoices):
        GOODS = 'GOODS', 'Товары'
        SERVICES = 'SERVICES', 'Услуги'
        HIRING = 'HIRING', 'Найм'

    category = models.CharField(max_length=10,
                                choices=Category.choices,
                                default=Category.GOODS)

    title = models.CharField(max_length=100)
    description = models.TextField(max_length=5000)
    image = models.ImageField(blank=True)
    date_posted = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey('usersapp.User', on_delete=models.CASCADE, null=False)

    slug = models.SlugField(max_length=100,
                            null=True,
                            unique=True,
                            db_index=True,
                            verbose_name='URL')


class Feedback(models.Model):
    # I dunno what to do with my imports, but they're not working.
    # So I did Foreignkeys like this.
    # "from usersapp.models import User" smth like this doesn't work, what do I do?
    # It didn't work in any of my last projects HEEEEEEEELP
    user = models.ForeignKey('usersapp.User', on_delete=models.CASCADE, null=False)
    advert = models.ForeignKey(Advertisment, on_delete=models.CASCADE, null=False)
    text = models.TextField(max_length=5000)
    image = models.ImageField(blank=True)
    date_posted = models.DateTimeField(default=timezone.now)
