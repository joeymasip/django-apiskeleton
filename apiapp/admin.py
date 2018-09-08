from django.contrib import admin
from .models import *

admin.site.site_header = 'API Administration'

class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'is_active')


admin.site.register(User, UserAdmin)