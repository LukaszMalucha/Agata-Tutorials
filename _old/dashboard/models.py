from django.db import models

class PropertyModel(models.Model):
    location=models.CharField(max_length=254)
    property_type=models.CharField(max_length=254)
    bedrooms=models.IntegerField(default=1)
    bathrooms=models.IntegerField(default=1)
    price=models.DecimalField(decimal_places=2, max_digits=12)
    sold=models.BooleanField(default=False)

    def __str__(self):
        return f"Property: {self.location} {self.price}"


