from django.db import models
from django.urls import reverse
from django.utils import timezone

from .advert import Advertisment
from .company import Company


class Feedback(models.Model):
    user = models.ForeignKey('usersapp.User',
                             on_delete=models.CASCADE,
                             null=True)
    # I wouldn't do another model just to separate feedbacks for company and advert feedbacks.
    # So we are using null=True for both.
    advert = models.ForeignKey(Advertisment,
                               on_delete=models.CASCADE,
                               null=True
                               )

    company = models.ForeignKey(Company,
                                on_delete=models.CASCADE,
                                null=True)

    text = models.TextField(max_length=5000)
    image = models.ImageField(blank=True)
    date_posted = models.DateTimeField(default=timezone.now)

    def get_absolute_url(self):
        return reverse('marketapp:advert_page', kwargs={'slug': self.advert})