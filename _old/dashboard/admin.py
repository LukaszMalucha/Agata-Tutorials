from django.contrib import admin
from dashboard.models import PropertyModel

class PropertyModelAdmin(admin.ModelAdmin):
    pass


admin.site.register(PropertyModel,PropertyModelAdmin)


