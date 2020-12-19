
from django.contrib import admin

# Local Django
from . models import Institute, Department, Course

# Register your models here.


class InstituteAdmin(admin.ModelAdmin):
    list_display = ('user', 'name', 'website')
    list_display_links = ('user', 'name', 'website')
    search_fields = ('user', 'name', 'short_name')


class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('department_name', 'institute',)
    list_display_links = ('department_name', 'institute',)
    search_fields = ('department_name', 'institute',)


class CourseAdmin(admin.ModelAdmin):
    list_display = ('institute', 'department', 'course')
    list_display_links = ('institute', 'department', 'course',)
    search_fields = ('institute', 'department', 'course',)


admin.site.register(Institute, InstituteAdmin)
admin.site.register(Department, DepartmentAdmin)
admin.site.register(Course, CourseAdmin)
