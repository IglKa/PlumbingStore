from django.db import models
from django.utils import timezone

from .star import Star


class Feedback(models.Model):
    user = models.ForeignKey('usersapp.User',
                             on_delete=models.CASCADE,
                             null=True)

    text = models.TextField(max_length=5000)
    image = models.ImageField(blank=True)
    date_posted = models.DateTimeField(default=timezone.now)

    star_given = models.ForeignKey(Star,
                                   null=True,
                                   on_delete = models.PROTECT)

    def __str__(self):
        return f'{self.star_given}'
