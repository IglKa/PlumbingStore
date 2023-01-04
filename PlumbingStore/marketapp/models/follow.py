from django.db import models
from django.urls import reverse

from .company import Company


class Follow(models.Model):
    company = models.ForeignKey(Company,
                                on_delete=models.CASCADE,
                                blank=True,
                                null=True,
                                )
    user = models.ForeignKey('usersapp.User',
                             on_delete=models.CASCADE,
                             null=True,
                             blank=True,
                             )

    def get_absolute_url(self):
        return reverse('marketapp:company', kwargs={'slug', self.company.slug})
