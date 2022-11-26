from django.conf import settings
from django.db import models
from django.urls import reverse
from django.utils import timezone

from autoslug.fields import AutoSlugField


class Advertisment(models.Model):
    class Category(models.TextChoices):
        GOODS = 'GOODS', 'Товары'
        SERVICES = 'SERVICES', 'Услуги'
        VACANCY = 'VACANCY', 'Вакансия'
        slug = models.SlugField(max_length=40,
                                unique=False,
                                db_index=True,
                                verbose_name='URL'
                                )

    category = models.CharField(max_length=40,
                                choices=Category.choices,
                                default=Category.GOODS
                                )
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=5000)
    image = models.ImageField(blank=True)
    date_posted = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)

    # Gives advertisment a slug automatically
    # TODO: Refactor, provide more useful logic
    slug = AutoSlugField(max_length=100,
                         populate_from='title',
                         unique_with=('title', 'date_posted'),
                         unique=True,
                         db_index=True,
                         verbose_name='URL')

    def get_absolute_url(self):
        return reverse('adverts/', kwargs={'adv_slug': self.slug})


class Feedback(models.Model):
    user = models.ForeignKey('usersapp.User', on_delete=models.CASCADE, null=True)
    advert = models.ForeignKey(Advertisment, on_delete=models.CASCADE, null=False)
    text = models.TextField(max_length=5000)
    image = models.ImageField(blank=True)
    date_posted = models.DateTimeField(default=timezone.now)
