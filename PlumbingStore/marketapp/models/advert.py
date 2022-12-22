from django.db import models
from django.urls import reverse
from django.utils import timezone

from .company import Company


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
    company = models.ForeignKey(Company, on_delete=models.CASCADE, null=True)

    slug = models.SlugField(
                            max_length=100,
                            unique=True,
                            db_index=True,
                            verbose_name='URL'
                            )

    star_rating = models.ForeignKey('Rating', on_delete=models.CASCADE, null=True)

    def get_absolute_url(self):
        # Will return to company that advert belongs to.
        return reverse('marketapp:company', kwargs={'slug': self.company})

    def __str__(self):
        return self.slug


class Star(models.Model):
    value = models.SmallIntegerField()

    def __str__(self):
        return str(self.value)


class Rating(models.Model):
    star = models.ForeignKey(Star, on_delete=models.PROTECT)
    advert = models.ForeignKey(Advertisment, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.advert} - {self.star}'