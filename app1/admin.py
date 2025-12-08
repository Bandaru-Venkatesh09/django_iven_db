from django.contrib import admin

from app1.models import employee

class emp_adm(admin.ModelAdmin):
    list_display=['Name','Pin','email']
admin.site.register(employee,emp_adm)
