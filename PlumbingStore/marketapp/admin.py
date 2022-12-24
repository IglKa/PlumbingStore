from django.contrib import admin
from django.db import models

from .models import Advertisment,\
                    Feedback, \
                    Company, \
                    Star, \
                    AdvertCategory, \
                    CompanyCategory


admin.site.register(Feedback)
admin.site.register(AdvertCategory)
admin.site.register(CompanyCategory)

@admin.register(Advertisment)
class AdvertAdmin(admin.ModelAdmin):
    list_display = ['category', 'company', 'title',
                    'description', 'date_posted', 'slug',
                    'star_rating'
                    ]


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ['category', 'name',
                    'descr', 'date_created', 'slug'
                    ]


admin.site.register(Star)