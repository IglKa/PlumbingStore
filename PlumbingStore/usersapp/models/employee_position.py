from django.db import models


class EmployeePosition(models.Model):
    """
    Employee categories and position.

    The Mangers group will have a choice between existing positions and
    if they don't find their needed one they could write it down
    and create a "custom" position. Lately, admin will check and rework
    this position if necessary(give it category, rename it and even delete).
    """

    position_category = models.ForeignKey('self',
                               on_delete=models.CASCADE,
                               blank=True,
                               null=True)

    position = models.CharField(max_length=100)

    def __str__(self):
        if self.position_category:
            return f'{self.position_category} - {self.position}'
        return f'{self.position}'
