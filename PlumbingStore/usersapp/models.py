from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse

from marketapp.models import Company


class EmployeePosition(models.Model):
    # Also adding employee position field, so client can recognize from who he is buying goods.
    position = models.CharField(max_length=40)

    def __str__(self):
        return f'{self.position}'


class User(AbstractUser):
    # There is no need to use username in site, so we will use email as username.
    username = models.CharField(max_length=45,
                                blank=True,
                                unique=False,
                                default=None,
                                null=True
                                )
    email = models.EmailField(blank=False,
                              unique=True,
                              max_length=194
                              )
    phone_number = models.DecimalField(max_digits=11,
                                       decimal_places=0,
                                       blank=True,
                                       default=None,
                                       null=True
                                       )

    employee_position = models.ForeignKey(EmployeePosition,
                                          on_delete=models.SET_NULL,
                                          blank=True,
                                          null=True
                                          )

    # Company where user works
    company = models.ForeignKey(Company,
                                on_delete=models.CASCADE,
                                null=True,
                                blank=True
                                )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]
