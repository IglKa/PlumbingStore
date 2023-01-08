from django.contrib import admin

from .models import User, EmployeePosition


admin.site.register(User)
admin.site.register(EmployeePosition)