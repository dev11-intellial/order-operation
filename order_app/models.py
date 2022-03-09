from django.db import models

# Create your models here.
class Customer(models.Model):
    first_name=models.CharField(max_length=25)
    last_name=models.CharField(max_length=25)
    contact_no=models.IntegerField()
    pincode=models.IntegerField()

    def __str__(self):
        return self.first_name

class Product(models.Model):
    
    name=models.CharField(max_length=25)
    unit_price=models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

class Order(models.Model):
    customer=models.ForeignKey(Customer, on_delete = models.CASCADE)
    product=models.ForeignKey(Product, on_delete = models.CASCADE)
    price =models.DecimalField(max_digits=10, decimal_places=2)
    qty=models.IntegerField()
    total_price=models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
