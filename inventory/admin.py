from django.contrib import admin

# Register your models here.
from .models import Warehouse

class WarehouseAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'company')
    list_filter = ('company',)
    search_fields = ('name', 'address', 'company__name')

admin.site.register(Warehouse, WarehouseAdmin)
