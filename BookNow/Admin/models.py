from django.db import models

# Create your models here..
class Admin(models.Model):
    id=models.IntegerField(primary_key=True,blank=False)
    name=models.CharField(max_length=50,blank=False)
    email=models.EmailField(unique=True,blank=False)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
