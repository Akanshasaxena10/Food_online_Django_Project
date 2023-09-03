from django.contrib import admin
from .models import User,UserProfile ##to register user
from django.contrib.auth.admin import UserAdmin
# Register your models here.

class CustomUserAdmin(UserAdmin):##to make password non-editable---readonly and other fields
    list_display = ('email', 'first_name', 'last_name', 'username', 'role', 'is_active')
    ordering = ('-date_joined',)
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(User,CustomUserAdmin)
admin.site.register(UserProfile)