from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.TextChoices):
    COMPUTER = 'COMPUTER',
    PHONE = 'PHONE',
    HOME = 'HOME',
    FOOD = "FOOD",
    KIDS = 'KIDS'

class Product(models.Model):
    name = models.CharField(max_length=30,default='Enter Item Name', blank=False)
    description = models.TextField(max_length=1000, default='Desc', blank=False)
    price = models.DecimalField(max_digits=7, decimal_places=2, blank= False)
    brand = models.CharField(max_length= 100, default='Enter Your Brand', blank=False)
    category = models.CharField(max_length = 30, default='', choices=Category.choices)
    ratings = models.DecimalField(max_digits=3, decimal_places=2, blank=True, default = 0)
    stock = models.IntegerField(default=0)
    createAt = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name
