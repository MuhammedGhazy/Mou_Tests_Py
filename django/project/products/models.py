from django.db import models
from datetime import datetime

# Create your models here.
class Product(models.Model):
    x = [
        ('phone','phone'),
        ('computer','computer'),
    ]
    name = models.CharField(max_length=50)
    content = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    image = models.ImageField(upload_to='photos/%y/%m/%d')
    acvtive = models.BooleanField(default=True)
    category = models.CharField(max_length=50, null=True, blank=True, choices=x)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['-price']

class Test(models.Model):
    date = models.DateField()
    time = models.TimeField(null = True)
    created = models.DateTimeField(default = datetime.now())