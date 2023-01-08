from django.contrib import admin

from .models import User, UserPosition, Profile


admin.site.register(User)
admin.site.register(UserPosition)
admin.site.register(Profile)
