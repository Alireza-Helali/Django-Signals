from django.db import models
from order.models import Order


# Create your models here.

class Sale(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    amount = models.PositiveIntegerField(null=True, blank=True)

    def __str__(self):
        return self.order.name
