from django.contrib import admin
from django.db import models

from .models import Advertisment, Feedback, Company, Rating, Star


admin.site.register(Feedback)


@admin.register(Advertisment)
class AdvertAdmin(admin.ModelAdmin):
    list_display = ['category', 'company', 'title',
                    'description', 'date_posted', 'slug'
                    ]
    # prepopulated_fields = {'slug': ('category', 'title')}


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ['category', 'holder', 'name',
                    'descr', 'date_created', 'slug'
                    ]


@admin.register(Rating)
class AdminRating(admin.ModelAdmin):
    list_display = ['star', 'advert']

admin.site.register(Star)