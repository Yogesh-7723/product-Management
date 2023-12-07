from django.db import models

# Create your models here.

class Shopkiper(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    mobile = models.CharField(max_length=100)
    shoop_name = models.CharField(max_length=200)
    password = models.CharField(max_length=200)

class Product(models.Model):
    title = models.CharField(max_length=100,blank=True)
    discription = models.TextField()
    pro_img  = models.FileField(upload_to='upload/',blank=True)