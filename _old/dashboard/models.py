from django.db import models

class PropertyModel(models.Model):
    """ Model for property """
    name=models.CharField(max_length=255)
    city=models.CharField(max_length=255)
    price=models.DecimalField(decimal_places=2, max_digits=12)
    sold=models.BooleanField(default=False)


