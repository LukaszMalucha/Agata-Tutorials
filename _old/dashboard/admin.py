from django.contrib import admin
from dashboard.models import PropertyModel

# Register your models here.
class PropertyModelAdmin(admin.ModelAdmin):
    pass

admin.site.register(PropertyModel, PropertyModelAdmin)

