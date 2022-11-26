from django.contrib import admin
from django.db import models

from .models import Advertisment, Feedback


admin.site.register(Feedback)


@admin.register(Advertisment)
class AdvertAdmin(admin.ModelAdmin):
    list_display = ['category', 'user', 'title',
                    'description', 'date_posted', 'slug'
                    ]
    prepopulated_fields = {'slug': ('category', 'title')}
