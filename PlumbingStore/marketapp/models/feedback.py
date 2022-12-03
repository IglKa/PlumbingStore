from django.db import models

import Advertisment
import Company


class Feedback(models.Model):
    user = models.ForeignKey('usersapp.User', on_delete=models.CASCADE, null=True)
    advert = models.ForeignKey(Advertisment, on_delete=models.CASCADE, null=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, null=True)
    text = models.TextField(max_length=5000)
    image = models.ImageField(blank=True)
    date_posted = models.DateTimeField(default=timezone.now)