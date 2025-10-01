from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    form = CustomUserChangeForm
    # fieldsets = UserAdmin.fieldsets
    add_form = CustomUserCreationForm
    # add_fieldsets = None
    # ordering = ()
    # list_display = ()


admin.site.register(CustomUser, CustomUserAdmin)
