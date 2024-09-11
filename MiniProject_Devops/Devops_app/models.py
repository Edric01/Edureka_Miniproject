from django.db import models

# Create your models here.
class Messsage(models.Model):
    Name=models.CharField(max_length=20)
    Email=models.EmailField()
    MessageText=models.TextField()

class Service(models.Model):
    Name=models.CharField(max_length=20)
    Description=models.TextField()
    price=models.IntegerField()