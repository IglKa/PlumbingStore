from django.contrib import admin

from .models import Advertisment, AdvertCategory, \
    Company, CompanyCategory


admin.site.register(AdvertCategory)
admin.site.register(Company)
admin.site.register(CompanyCategory)


@admin.register(Advertisment)
class AdvertAdmin(admin.ModelAdmin):
    list_display = ['category', 'company', 'title',
                    'description', 'date_posted', 'slug',
                    'rating'
                    ]
