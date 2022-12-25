from django.db import models
from django.urls import reverse
from django.utils import timezone

from .star import Star


class Feedback(models.Model):
    user = models.ForeignKey('usersapp.User',
                             on_delete=models.CASCADE,
                             null=True)
    # Leave it denormalized so it's easier for search in feedback section
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
        return f'{self.advert}: {self.star_given}'

    def get_absolute_url(self):
        return reverse('marketapp:advert-page', kwargs={'slug': self.advert})
