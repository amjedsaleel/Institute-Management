from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext, gettext_lazy as _
from django.contrib.auth import get_user_model

# Register your models here.


class CustomUserAdmin(UserAdmin):
    fieldsets = (
        (None, {'fields': ('username', 'email', 'password')}),

        (_('User Status'), {
            'fields': ('is_student', 'is_teacher', 'is_institute',),
        }),

        (_('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions',),
        }),

        (_('Important dates'), {'fields': ('date_joined', )}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2'),
        }),
    )

    list_display = ('username', 'email', 'is_institute', 'is_teacher', 'is_student',)
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups')
    search_fields = ('username', 'email')
    ordering = ('username',)


admin.site.register(get_user_model(), CustomUserAdmin)

