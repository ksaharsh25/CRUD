from django.db import models

# Create your models here.
class Customer(models.Model):
    Name=models.CharField(max_length=50,blank=True)
    Address=models.TextField(max_length=500,blank=True)
    City=models.CharField(max_length=50,blank=True)
    State=models.CharField(max_length=20,blank=True)
    Mobile=models.IntegerField(max_length=50,blank=True)
    EmailId=models.EmailField(max_length=50,blank=True)
    Password=models.CharField(max_length=50,blank=True)

class Vendor(models.Model):
    Name=models.CharField(max_length=50,blank=True)
    Address=models.TextField(max_length=500,blank=True)
    City=models.CharField(max_length=50,blank=True)
    State=models.CharField(max_length=20,blank=True)
    Mobile=models.IntegerField(max_length=50,blank=True)
    EmailId=models.EmailField(max_length=50,blank=True)
    Password=models.CharField(max_length=50,blank=True)