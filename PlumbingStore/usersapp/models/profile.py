from django.db import models

from marketapp.models import Company
from .employee_position import EmployeePosition
from .user import User


class Profile(models.Model):
    """Main profile model."""

    user = models.OneToOneField(User,
                                on_delete=models.CASCADE)

    company = models.ForeignKey(Company,
                                on_delete=models.SET_NULL,
                                blank=True,
                                null=True,
                                )

    position = models.ForeignKey(EmployeePosition,
                                 blank=True,
                                 null=True,
                                 on_delete=models.SET_NULL)

    def __str__(self):
        return f'{self.pk} - {self.user}'
