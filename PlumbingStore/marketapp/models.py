from django.db import models
from django.urls import reverse
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
                            null=True,
                            unique=True,
                            db_index=True,
                            verbose_name='URL')

    def get_absolute_url(self):
        return reverse('marketapp:advert_page', kwargs={'pk': self.pk})


class Feedback(models.Model):
    user = models.ForeignKey('usersapp.User', on_delete=models.CASCADE, null=True)
    advert = models.ForeignKey(Advertisment, on_delete=models.CASCADE, null=False)
    text = models.TextField(max_length=5000)
    image = models.ImageField(blank=True)
    date_posted = models.DateTimeField(default=timezone.now)
