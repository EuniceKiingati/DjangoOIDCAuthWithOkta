from django.db import models

# Create your models here.
from customers.models import Customer

class Order(models.Model):
    item = models.CharField(max_length=100)
    amount = models.IntegerField()
    time = models.DateTimeField()
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    #if a customer is deleted, all associated orders are deleted

    def __str__(self):
        return f"{self.item} - {self.customer.name} ({self.customer.email})"