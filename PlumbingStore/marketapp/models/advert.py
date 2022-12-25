from django.db import models
from django.urls import reverse
from django.utils import timezone

import utils
from .company import Company


class AdvertCategory(models.Model):
    """Advert category"""

    # Remade it like this because some categories might be not in the list.
    # I'll do mechanism on form field that will be providing function to choose category firstly
    # and then if user couldn't see the needed category he could create it himself.
    category_name = models.CharField(max_length=40)

    def __str__(self):
        return f'{self.category_name}'


class Advertisment(models.Model):
    # I will leave this like this, so the company name can be showed on post easily
    company = models.ForeignKey(Company,
                                on_delete=models.CASCADE,
                                null=True,
                                to_field='slug')

    category = models.ForeignKey(AdvertCategory,
                                 on_delete=models.PROTECT,
                                 null=True,
                                 help_text="Choose category of your Advertisment. If it's not in the list just write it down and it will be created in our Data Base for future uses",
                                 )

    title = models.CharField(max_length=150)
    description = models.TextField(max_length=5000)
    image = models.ImageField(blank=True)
    date_posted = models.DateTimeField(default=timezone.now)

    slug = models.SlugField(max_length=100,
                            unique=True,
                            db_index=True,
                            verbose_name='URL'
                            )
    # TODO: End it up
    # First time creating this type of Fields.
    star_rating = utils.AdvertRatingField(slug=slug,
                                          null=True,)

    def get_absolute_url(self):
        # Will return to company that advert belongs to.
        return reverse('marketapp:company', kwargs={'slug': self.company})

    def __str__(self):
        return f'{self.slug}'
