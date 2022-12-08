from django.db import models

# Create your models here.
class SellerModel(models.Model):
    Name=models.CharField(max_length=255)
    Gender=models.CharField(max_length=25)
    Address=models.CharField(max_length=500)
    DOB=models.CharField(max_length=50)
    Country=models.CharField(max_length=255)
    Phone=models.CharField(max_length=20)
    Username=models.CharField(max_length=255)
    Password=models.CharField(max_length=50)
    ImageFile=models.FileField()
    Status=models.CharField(max_length=10,default='pending')

class ProductModel(models.Model):
    Name=models.CharField(max_length=255)
    ImageFile=models.FileField()
    Details=models.CharField(max_length=500)
    Stock=models.IntegerField()
    Category=models.ForeignKey('siteAdmin.categoryTableModel',on_delete=models.CASCADE)
    Seller=models.ForeignKey(SellerModel,on_delete=models.CASCADE)
    Price=models.IntegerField()

class TrackingModel(models.Model):
    Order=models.ForeignKey('buyer.OrderModel', on_delete=models.CASCADE)
    Date=models.CharField(max_length=10)
    Time=models.CharField(max_length=10)
    Details=models.CharField(max_length=500)
