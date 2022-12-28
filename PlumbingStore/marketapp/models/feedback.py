from django.db import models
from django.urls import reverse
from django.utils import timezone

from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType


class Feedback(models.Model):
    class Star(models.IntegerChoices):
        FIVE = 5
        FOUR = 4
        THREE = 3
        TWO = 2
        ONE = 1

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

    text = models.TextField(max_length=5000)
    image = models.ImageField(blank=True)
    date_posted = models.DateTimeField(default=timezone.now)

    rating = models.IntegerField(choices=Star.choices,
                                 default=Star.ONE
                                 )

    def __str__(self):
        return f'{self.content_object} - {self.rating}'

    def get_absolute_url(self):
        return reverse('marketapp:advert-page', kwargs={'slug': self.content_object__slug})
