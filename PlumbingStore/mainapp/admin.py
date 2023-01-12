from django.contrib import admin

from .models import Advertisment, AdvertCategory


admin.site.register(AdvertCategory)


@admin.register(Advertisment)
class AdvertAdmin(admin.ModelAdmin):
    list_display = ['category', 'company', 'title',
                    'description', 'date_posted', 'slug',
                    'rating'
                    ]
