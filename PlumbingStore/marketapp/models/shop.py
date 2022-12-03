from django.db import models
from django.utils import timezone


class Company(models.Model):
    class Category(models.TextChoices):
        SHOP = 'SHOP', 'Shop'
        STARTUP = 'STARTUP', 'Startup'
        BUSINESS = 'BUSINESS', 'Business'

    holder = models.ForeignKey('usersapp.User', on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=50, blank=False)
    descr = models.TextField(max_length=5000, blank=False)
    header_image = models.ImageField(blank=True)
    profile_image = models.ImageField(blank=True)
    date_created = models.DateTimeField(default=timezone.now)

    category = models.CharField(max_length=10,
                                choices=Category.choices,
                                default=Category.SHOP
                                )

    slug = models.SlugField(max_length=100,
                            unique=True,
                            db_index=True,
                            verbose_name='URL'
                            )