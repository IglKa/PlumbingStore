from django.db import models

from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    # There is no need to use username in site, so we will use email as username.
    username = models.CharField(max_length=45,
                                blank=True,
                                unique=False,
                                default=None,
                                null=True)

    email = models.EmailField(blank=False,
                              unique=True,
                              max_length=194)

    phone_number = models.DecimalField(max_digits=11,
                                       decimal_places=0,
                                       blank=True,
                                       default=None,
                                       null=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    def __str__(self):
        return f'{self.email}'
