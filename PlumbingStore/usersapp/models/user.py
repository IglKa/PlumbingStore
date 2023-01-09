from django.db import models

from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """
    User model.

    Phone number there will be necessary for phone calls between users
    (and if I am going to be in the mood, I'll try to do this in site).
    Usernames are not necessary, because the type of my site needs emails
    firstly than nicknames(I think so).
    """

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

    # As I said, here is no need to use username on site, so we will use email as username.
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    def __str__(self):
        return f'{self.email}'
