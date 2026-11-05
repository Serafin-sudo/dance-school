from django.contrib import admin
from .models import School

class SchoolAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "street", "city", "province", "zip", "country", "website", "phone", "email", "vat"]

admin.site.register(School, SchoolAdmin)