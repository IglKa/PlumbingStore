from django.contrib import admin
from django.db import models

from .models import Advertisment, Feedback, Company, Star


admin.site.register(Feedback)


@admin.register(Advertisment)
class AdvertAdmin(admin.ModelAdmin):
    list_display = ['category', 'company', 'title',
                    'description', 'date_posted', 'slug'
                    ]


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ['category', 'name',
                    'descr', 'date_created', 'slug'
                    ]


admin.site.register(Star)