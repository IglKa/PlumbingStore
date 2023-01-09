from django.db import models
from django.urls import reverse
from django.utils import timezone

from django.contrib.contenttypes.fields import GenericRelation

from .feedback import Feedback


class CompanyCategory(models.Model):
    """Company category"""

    # Same as with advert categories
    category_name = models.CharField(max_length=30)

    def __str__(self):
        return f'{self.category_name}'


class Company(models.Model):
    category = models.ForeignKey(CompanyCategory,
                                 null=True,
                                 on_delete=models.PROTECT,
                                 help_text="Choose category of your Company. If it's not in the list just write it down and it will be created in our Data Base for future uses"
                                 )

    name = models.CharField(max_length=50,
                            blank=False
                            )

    descr = models.TextField(max_length=5000,
                             blank=False
                             )

    header_image = models.ImageField(blank=True)
    profile_image = models.ImageField(blank=True)
    date_created = models.DateTimeField(default=timezone.now)

    slug = models.SlugField(max_length=100,
                            unique=True,
                            db_index=True,
                            verbose_name='URL'
                            )

    rating = models.FloatField(null=True,
                               blank=True
                               )

    feedbacks = GenericRelation(Feedback,
                                related_query_name='company_feedbacks'
                                )

    def get_absolute_url(self):
        return reverse('marketapp:company', kwargs={'slug': self.slug})

    def __str__(self):
        return f'{self.slug}'


class CompanyHolder(models.ForeignKey):
    holder = models.ForeignKey('usersapp.User',
                               on_delete=models.CASCADE,
                               null=True
                               )

    company = models.ForeignKey(Company,
                                on_delete=models.CASCADE,
                                null=True
                                )

    def __str__(self):
        return f'{self.holder} - {self.company}'
