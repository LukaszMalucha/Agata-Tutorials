from django.db import models

class PropertyModel(models.Model):
    area=models.CharField(max_length=254)
    property_type=models.CharField(max_length=254)
    bedrooms=models.IntegerField(default=1)
    bathrooms = models.IntegerField(default=1)
    price=models.DecimalField(max_digits=8,decimal_places=2)
    sold=models.BooleanField(default=False)

    def __str__(self):
        return f"{self.area} property"
