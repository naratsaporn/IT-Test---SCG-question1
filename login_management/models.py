from django.db import models
from django.utils.timezone import datetime
class Order(models.Model):
    price_totol = models.DecimalField(max_digits=5, decimal_places=2)
    date_sell = models.DateTimeField(default=datetime.now, blank=True)

class Transaction(models.Model):
    
    product_name = models.CharField(max_length=120)
    quantity = models.IntegerField(default=0 )
    price = models.DecimalField(max_digits=5, decimal_places=2)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    date_sell = models.DateTimeField(default=datetime.now, blank=True)
