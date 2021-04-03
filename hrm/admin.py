from django.contrib import admin
from .models import Department,Division
# Register your models here.

class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('__str__','name','description')
    list_filter = ('name',)
    list_editable = ('name',)
    list_per_page = 10
admin.site.register(Department)

class DivisionAdmi(admin.ModelAdmin):
    list_display = ('name','department','description')
    list_filter = ('name','department')
    list_editable = ('name','department')
    list_per_page = 10
admin.site.register(Division)