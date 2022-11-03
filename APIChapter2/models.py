from django.db import models

# Create your models here.
class Customer(models.Model):
    Name=models.CharField(max_length=50,blank=True)
    Address=models.TextField(max_length=500,blank=True)
    City=models.CharField(max_length=50,blank=True)
    State=models.CharField(max_length=20,blank=True)
    Mobile=models.IntegerField(max_length=50,blank=True)
    EmailId=models.EmailField()
    Password=models.CharField(max_length=50,blank=True)
    id=models.IntegerField(max_length=50,blank=True,primary_key=True)
    def __str__(self): 
        return self.Name

class Vendor(models.Model):
    Name=models.CharField(max_length=50,blank=True)
    Address=models.TextField(max_length=500,blank=True)
    City=models.CharField(max_length=50,blank=True)
    State=models.CharField(max_length=20,blank=True)
    Mobile=models.IntegerField(max_length=50,blank=True)
    EmailId=models.EmailField(max_length=50,blank=True)
    Password=models.CharField(max_length=50,blank=True)