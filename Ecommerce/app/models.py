from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Phone(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10,decimal_places=0)
    available = models.BooleanField(default=True)
    image_path = models.CharField(max_length=255) 
    rating = models.IntegerField(default=0)

    
    def __str__(self):
        return f"{self.name} - ${self.price}"
    class Meta:
        verbose_name_plural = "Phones"

class Device(models.Model):
    phone_id = models.ForeignKey(Phone,on_delete=models.CASCADE)
    model = models.CharField(max_length=40)
    display = models.CharField(max_length=35)
    resolution = models.CharField(max_length=20)
    processor = models.CharField(max_length=35)
    ram = models.CharField(max_length=15)  
    storage = models.CharField(max_length=50) 
    rear_camera = models.CharField(max_length=50)
    front_camera = models.CharField(max_length=15)
    battery = models.CharField(max_length=15)  
    operating_system = models.CharField(max_length=27)
    dimensions = models.CharField(max_length=32)  
    weight = models.CharField(max_length=25)  
    connectivity = models.CharField(max_length=30)
    colors = models.CharField(max_length=60)  

    def __str__(self):
        return self.model

class Orders(models.Model):
    phone_id = models.ForeignKey(Phone,on_delete=models.CASCADE)
    customer_id = models.ForeignKey(User,on_delete=models.CASCADE)
    customer_address = models.CharField(max_length=200)
    customer_city = models.CharField(max_length=50)
    customer_zip_code = models.CharField(max_length=5)
    order_date = models.DateTimeField(auto_now_add=True)
    customer_phone = models.CharField(max_length=11)
    status = models.CharField(max_length=20, default='Pending')
    
    def __str__(self):
        return f"Order for {self.phone_id.name} by {self.customer_id.username}"
    class Meta:
        verbose_name_plural = "Orders"