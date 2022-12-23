from django.db import models
from django.urls import reverse
from django.utils import timezone

from .advert import Advertisment, Star


class Feedback(models.Model):
    user = models.ForeignKey(
                             'usersapp.User',
                             on_delete=models.CASCADE,
                             null=True)
    advert = models.ForeignKey(
                               Advertisment,
                               on_delete=models.CASCADE,
                               null=True
                               )

    text = models.TextField(max_length=5000)
    image = models.ImageField(blank=True)
    date_posted = models.DateTimeField(default=timezone.now)

    star_given = models.ForeignKey(Star,
                                   on_delete=models.PROTECT,
                                   default=0,
                                   null=True)

    def get_absolute_url(self):
        return reverse('marketapp:advert_page', kwargs={'slug': self.advert})

    def __str__(self):
        return f'{self.advert}'


class FeedbackAdvert(models.Model):
    advert = models.ForeignKey(Advertisment, on_delete=models.CASCADE)
    star_given = models.ForeignKey(Feedback, on_delete=models.CASCADE)