from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
# Register your models here.

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = models.CustomUser
        fields = '__all__'
class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model  = models.CustomUser
        fields = '__all__'
@admin.register(models.CustomUser)
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    list_display = ("username", "email", "is_staff", "is_active", "thread_id")
    list_filter = ("is_staff", "is_active")

    
    fieldsets = (
        (None, {"fields": ("username",'first_name','last_name', "email", "password", "thread_id")}),
        ("Permissions", {"fields": ("is_staff", "is_superuser", "is_active", "groups", "user_permissions")}),
        ("Important dates", {"fields": ("last_login", "date_joined")}),
    )

    
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ("username", 'first_name','last_name', "email", "thread_id", "password1", "password2", "is_staff", "is_active"),
        }),
    )

    search_fields = ("username", "email")
    ordering = ("username",)
    filter_horizontal = ("groups", "user_permissions")