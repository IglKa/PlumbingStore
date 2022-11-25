from django.db import models
from django.utils import timezone
from django.conf import settings


class Advertisment(models.Model):

    class Category(models.TextChoices):
        GOODS = 'GOODS', 'Товары'
        SERVICES = 'SERVICES', 'Услуги'
        HIRING = 'HIRING', 'Найм'

    category = models.CharField(max_length=10,
                                choices=Category.choices,
                                default=Category.GOODS
                                )
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=5000)
    image = models.ImageField(blank=True)
    date_posted = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)

    slug = models.SlugField(max_length=100,
                            db_index=True,
                            unique=True,
                            verbose_name='URL')


class Feedback(models.Model):
    user = models.ForeignKey('usersapp.User', on_delete=models.CASCADE, null=True)
    advert_slug = models.ForeignKey(Advertisment, on_delete=models.CASCADE, null=False)
    text = models.TextField(max_length=5000)
    image = models.ImageField(blank=True)
    date_posted = models.DateTimeField(default=timezone.now)
