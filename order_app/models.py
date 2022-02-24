from django.db import models

# Create your models here.
class Customer(models.Model):
    first_name=models.CharField(max_length=25)
    last_name=models.CharField(max_length=25)
    contact_no=models.CharField(max_length=20)
    pincode=models.CharField(max_length=10)

    def __str__(self):
        return self.first_name

class Product(models.Model):
    
    name=models.CharField(max_length=25)
    unit_price=models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Order(models.Model):
    customer_id=models.ForeignKey(Customer, on_delete = models.CASCADE)
    product_id=models.ForeignKey(Product, on_delete = models.CASCADE)
    price =models.CharField(max_length=100)
    qty=models.CharField(max_length=100)
    total_price=models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
