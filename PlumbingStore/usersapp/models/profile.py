from django.db import models

from marketapp.models import Company


class Profile(models.Model):
    """Main profile model."""

    from .employee_position import EmployeePosition
    from .user import User

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
        return f'{self.user.email}'
