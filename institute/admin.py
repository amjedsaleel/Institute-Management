from django.contrib import admin

# Local Django
from . models import Institute

# Register your models here.


class InstituteAdmin(admin.ModelAdmin):
    list_display = ('user', 'name', 'website')
    list_display_links = ('user', 'name', 'website')
    search_fields = ('user', 'name', 'short_name')


admin.site.register(Institute, InstituteAdmin)
