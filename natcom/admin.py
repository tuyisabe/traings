from django.contrib import admin
from . import models

class CoursesAdmin(admin.ModelAdmin):
    list_display=('name','dept','credit','desc')
admin.site.register(models.Courses,CoursesAdmin)


