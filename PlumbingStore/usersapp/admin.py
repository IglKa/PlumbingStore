from django.contrib import admin

from .models import User, Profile, EmployeePosition


admin.site.register(User)
admin.site.register(EmployeePosition)
admin.site.register(Profile)
