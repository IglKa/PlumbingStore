from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse


class User(AbstractUser):
    # There is no need to use username in site, so we will use email as username.

    username = models.CharField(max_length=45, blank=True, unique=False, default=None, null=True)
    email = models.EmailField(blank=False, unique=True)
    phone_number = models.DecimalField(max_digits=11, decimal_places=0, blank=True, default=None, null=True)
    # Also adding employee status field, so client can recognize from who he is buying goods.

    class EmployeeStatus(models.TextChoices):
        SALES_MANAGER = 'SALES MANAGER', 'Менеджер по продажам'
        SELF_EMPLOYED = 'SELF EMPLOYED', 'Самозанятый'
        RESELLER = 'RESELLER', 'Перекуп'

    employee_status = models.CharField(max_length=15,
                                       choices=EmployeeStatus.choices,
                                       default=None,
                                       blank=True,
                                       null=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    def get_absolute_url(self):
        return reverse('marketapp:homepage')
