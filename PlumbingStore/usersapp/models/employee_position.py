from django.db import models

from django.contrib.auth.models import Group


class EmployeePosition(models.Model):
    """
    Employee categories and position.

    The Mangers group will have a choice between existing positions and
    if they don't find their needed one they could write it down
    and create a "custom" position. Lately, admin will check and rework
    this position if necessary(give it category, rename it and even delete).
    """

    position_group = models.ForeignKey(Group,
                                       on_delete=models.PROTECT,
                                       blank=True,
                                       null=True)

    position = models.CharField(max_length=100)

    def __str__(self):
        if self.position_group:
            return f'{self.position_group} - {self.position}'
        return f'{self.position}'
