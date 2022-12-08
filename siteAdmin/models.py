from django.db import models

# Create your models here.
class adminModel(models.Model):
    Username=models.CharField(max_length=255)
    Password=models.CharField(max_length=255)

class categoryTableModel(models.Model):
    Category=models.CharField(max_length=255)