from django.contrib.auth.models import AbstractUser
from django.db import models

from marketapp.models import Company


class TypeOfActivity(models.TextChoices):
    SELF_EMPLOYED = 'SELF-EMPLOYED', 'Self-employed'
    COMPANY_PERSONNEL = 'COMPANY PERSONNEL', 'Company personnel'
    NOT_A_WORKER = 'NOT A WORKER', 'Consumer' # Represents a user that is off the work or just a Customer


class EmployeePosition(models.Model):
    """
    Employee position.
    Will show the user type of activity
    (he might be either self-employed or a company personnel).
    """

    type_of_activity = models.CharField(choices=TypeOfActivity.choices,
                                        default=TypeOfActivity.NOT_A_WORKER,
                                        max_length=20,
                                        )

    position = models.CharField(max_length=40,
                                null=True,
                                blank=True)

    def __str__(self):
        if self.type_of_activity == 'NOT A WORKER':
            return f'{self.type_of_activity} | off the work'
        return f'{self.type_of_activity} - {self.position}'


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
    # Company where user works
    company = models.ForeignKey(Company,
                                on_delete=models.CASCADE,
                                null=True,
                                blank=True
                                )
    position = models.ForeignKey(EmployeePosition,
                                    blank=True,
                                    null=True,
                                    on_delete=models.SET_NULL,
                                    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    def __str__(self):
        return f'{self.email}'
