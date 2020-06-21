from django.contrib import admin

from dashboard.models import PropertyModel


class PropertyModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')



admin.site.register(PropertyModel, PropertyModelAdmin)
