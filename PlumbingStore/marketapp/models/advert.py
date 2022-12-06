from django.conf import settings
from django.db import models
from django.urls import reverse
from django.utils import timezone


class Advertisment(models.Model):
    class Category(models.TextChoices):
        GOODS = 'GOODS', 'Товары'
        SERVICES = 'SERVICES', 'Услуги'
        VACANCY = 'VACANCY', 'Вакансия'

    category = models.CharField(
                                max_length=15,
                                choices=Category.choices,
                                default=Category.GOODS
                                )
    title = models.CharField(max_length=150)
    description = models.TextField(max_length=5000)
    image = models.ImageField(blank=True)
    date_posted = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)

    slug = models.SlugField(
                            max_length=100,
                            unique=True,
                            db_index=True,
                            verbose_name='URL'
                            )

    def get_absolute_url(self):
        return reverse('', kwargs={'adv_slug': self.slug})
