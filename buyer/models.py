from django.db import models

# Create your models here.
class BuyerModel(models.Model):
    Name=models.CharField(max_length=255)
    Gender=models.CharField(max_length=20)
    Address=models.CharField(max_length=500)
    DOB=models.CharField(max_length=50)
    Country=models.CharField(max_length=255)
    Phone=models.CharField(max_length=20)
    Username=models.CharField(max_length=255)
    Password=models.CharField(max_length=50)

class CartModel(models.Model):
    Buyer=models.ForeignKey(BuyerModel,on_delete=models.CASCADE)
    Product=models.ForeignKey('seller.ProductModel', on_delete=models.CASCADE)
    Shipping=models.CharField(max_length=500)
    Phone=models.CharField(max_length=50,default="123")
    Quantity=models.IntegerField()
    Total_price=models.IntegerField()

class OrderModel(models.Model):
    Seller=models.ForeignKey('seller.SellerModel',on_delete=models.CASCADE)
    Product=models.ForeignKey('seller.ProductModel',on_delete=models.CASCADE)
    Buyer=models.ForeignKey('buyer.BuyerModel',on_delete=models.CASCADE)
    Shipping=models.CharField(max_length=255)
    Phone=models.CharField(max_length=50,default='10')
    Quantity=models.IntegerField()
    Total_price=models.IntegerField()
    Date=models.CharField(max_length=50,default='10')
    Time=models.CharField(max_length=50)
    Status=models.CharField(max_length=50,default='pending')
