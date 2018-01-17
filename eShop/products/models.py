from django.db import models

# Create your models here.
#added as part of the project
class Product(models.Model):
    product_name = models.CharField(max_length=200)
    product_date = (models.DateTimeField)('date published')

#added as part of the project
class Prices(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    price_text = models.CharField(max_length=200)
    price = models.IntegerField(default=0)
