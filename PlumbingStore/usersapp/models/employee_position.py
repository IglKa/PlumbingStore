from django.db import models


class TypeOfActivity(models.TextChoices):
    """Users current status activity"""

    INDIVIDUAL_ENTREPRENEUR = 'INDIVIDUAL ENTREPRENEUR', 'Individual entrepreneur'
    COMPANY_PERSONNEL = 'COMPANY PERSONNEL', 'Company personnel'


class UserPosition(models.Model):
    """
    Employee position.
    Will show the user type of activity and position in company
    (he might be either self-employed or a company personnel).
    """

    type_of_activity = models.CharField(choices=TypeOfActivity.choices,
                                        default=TypeOfActivity.INDIVIDUAL_ENTREPRENEUR,
                                        max_length=23,
                                        )

    position = models.CharField(max_length=100,
                                null=True,
                                blank=True)

    def __str__(self):
        return f'{self.type_of_activity} - {self.position}'
