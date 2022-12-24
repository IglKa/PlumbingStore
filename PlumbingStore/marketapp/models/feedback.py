from django.db import models
from django.utils import timezone

from .star import Star


class Feedback(models.Model):
    user = models.ForeignKey('usersapp.User',
                             on_delete=models.CASCADE,
                             null=True)

    advert = models.ForeignKey('Advertisment',
                               null=True,
                               on_delete=models.CASCADE)

    text = models.TextField(max_length=5000)
    image = models.ImageField(blank=True)
    date_posted = models.DateTimeField(default=timezone.now)

    star_given = models.ForeignKey(Star,
                                   null=True,
                                   on_delete = models.PROTECT)

    def __str__(self):
        return f'{self.star_given}'

class FeedbackAdvert(models.Model):
    advert = models.ForeignKey('Advertisment',
                               on_delete=models.CASCADE,
                               null=True,
                               to_field='slug')

    feedback_star = models.ForeignKey('Feedback',
                                      on_delete=models.CASCADE,
                                      null=True)
    def __str__(self):
         return f'{self.advert} - {self.feedback_star}'
