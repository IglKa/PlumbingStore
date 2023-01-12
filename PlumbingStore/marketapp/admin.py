from django.contrib import admin

from .models import Advertisment, \
    Feedback, \
    Company, \
    AdvertCategory, \
    CompanyCategory, \
    Follow

admin.site.register(Feedback)
admin.site.register(AdvertCategory)
admin.site.register(CompanyCategory)
admin.site.register(Follow)


@admin.register(Advertisment)
class AdvertAdmin(admin.ModelAdmin):
    list_display = ['category', 'company', 'title',
                    'description', 'date_posted', 'slug',
                    'rating'
                    ]


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ['category', 'name',
                    'descr', 'date_created', 'slug',
                    'rating'
                    ]
