from django.db import models
from django.urls import reverse
from django.utils import timezone

from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

from .star import Star


class Feedback(models.Model):
    user = models.ForeignKey('usersapp.User',
                             on_delete=models.CASCADE,
                             null=True
                             )

    content_type = models.ForeignKey(ContentType,
                                     on_delete=models.CASCADE
                                     )

    object_id = models.PositiveIntegerField()

    content_object = GenericForeignKey('content_type',
                                       'object_id'
                                       )

    star_given = models.ForeignKey(Star,
                                   null=True,
                                   on_delete = models.PROTECT
                                   )

    text = models.TextField(max_length=5000)
    image = models.ImageField(blank=True)
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.advert}: {self.star_given}'

    def get_absolute_url(self):
        return reverse('marketapp:advert-page', kwargs={'slug': self.advert})
