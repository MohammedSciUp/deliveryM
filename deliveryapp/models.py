from django.db import models

class Deliverer(models.Model):
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)

    def __str__(self):
        return self.name

class Order(models.Model):
    order_number = models.CharField(max_length=20, unique=True)
    from_location = models.CharField(max_length=200)
    to_location = models.CharField(max_length=200)
    pick_up_location = models.CharField(max_length=200)
    pick_up_pic = models.ImageField(upload_to='pick_up_pics/', blank=True, null=True)
    pick_up_phone_number = models.CharField(max_length=15)
    pick_up_time = models.CharField(max_length=50)
    package_type = models.CharField(max_length=50)
    pick_up_comment = models.TextField(blank=True, null=True)
    delivery_location = models.CharField(max_length=200)
    delivery_pic = models.ImageField(upload_to='delivery_pics/', blank=True, null=True)
    delivery_phone_number = models.CharField(max_length=15)
    delivery_time = models.CharField(max_length=50)
    delivery_comment = models.TextField(blank=True, null=True)
    deliverer = models.ForeignKey(Deliverer, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"Order {self.order_number}"
