from django.db import models
from django.urls import reverse

from .company import Company


class Follow(models.Model):
    """
    User following company.

    This model represents follow(or subscribe? whatever) activity of user.
    Following company's ads will appear in mostly.
    And after user scrolled all following, the ones with high rating
    (recommendations) will appear.
    """

    company = models.ForeignKey(Company,
                                on_delete=models.CASCADE,
                                blank=True,
                                null=True,
                                )
    profile = models.ForeignKey('usersapp.Profile',
                                on_delete=models.CASCADE,
                                null=True,
                                blank=True,
                                )
