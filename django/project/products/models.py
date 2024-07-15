from django.db import models
from datetime import datetime

# Create your models here.
class Product (models.Model):
    x = [
        ('phone', 'phone'),
        ('computer', 'computer')
    ]
    name = models.CharField(max_length = 50, default = 'name')
    content = models.TextField(default='content', null=True, blank=True, verbose_name = 'Discription')
    price = models.DecimalField(max_digits= 10, decimal_places= 2, default = 1000)
    image = models.ImageField(upload_to='photos/%y/%m/%d', default= 'phptps/24/07/images.jpeg')
    active = models.BooleanField(default=True)
    category = models.CharField(max_length = 50, null = True, blank = True, choices = x)

    def __str__(self):
        return (self.name)
    
    class _Meta :
        verbose_name = 'name'

    class Meta:
        ordering = ['-price']

class test (models.Model):
    date = models.DateField(null = True,)
    time = models.TimeField(null = True,)
    created = models.DateTimeField(default = datetime.now)