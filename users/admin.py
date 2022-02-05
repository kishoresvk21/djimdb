from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .admin_custom_forms import UserCreationForm,UserChangeForm
from .models import CustomUser

class UserAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    form = UserChangeForm
    add_form = UserCreationForm

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = (
            'username',
            'id',
            'email',
            'firstname',
            'lastname',
            'mobile',
            'created_at',
            'updated_at',
            'is_staff',
            'is_active',
            'is_superuser',
        )
    list_filter = ('is_admin',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('firstname','lastname','mobile')}),
        ('Permissions', {'fields': ('is_admin','is_superuser','is_staff')}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username','firstname','lastname','mobile' ,'password1', 'password2'),
        }),
    )
    search_fields = ('email','username')
    ordering = ('email',)
    filter_horizontal = ()


admin.site.register(CustomUser, UserAdmin)
admin.site.unregister(Group)

