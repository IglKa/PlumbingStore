from django.db import models

from marketapp.models import Company
from .employee_position import UserPosition
from .user import User


class Profile(models.Model):
    class Status(models.TextChoices):
        LFJ = 'LOOKING FOR JOB', 'Looking for job'
        CUSTOMER = 'CUSTOMER', 'Customer'
        HAVE_JOB = 'HAVE JOB', 'Have job'

    user = models.OneToOneField(User,
                                on_delete=models.CASCADE)

    status = models.CharField(max_length=15,
                              choices=Status.choices,
                              default=Status.CUSTOMER)

    company = models.ForeignKey(Company,
                                on_delete=models.SET_NULL,
                                blank=True,
                                null=True,
                                )

    position = models.ForeignKey(UserPosition,
                                 blank=True,
                                 null=True,
                                 on_delete=models.SET_NULL)



    def __str__(self):
        return f'{self.user}'
