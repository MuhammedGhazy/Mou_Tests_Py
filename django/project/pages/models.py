from django.db import models

# Create your models here.
class Female(models.Model):
    name = models.CharField(max_length=50, null=True)
    
    def __str__(self):
        return self.name

class Male(models.Model):
    name = models.CharField(max_length=50, null=True)
    girls = models.OneToOneField(Female, on_delete= models.CASCADE)
    def __str__(self):
        return self.name
    
###########################
class Product(models.Model):
    title = models.CharField(max_length = 50, null = True)
    def __str__(self):
        return self.title
    
class User(models.Model):
    
    name = models.CharField(max_length = 50, null = True)
    products = models.ForeignKey(Product, on_delete=models.CASCADE)
    def __str__(self):
        return self.name
    
    ###########################
class Viedo(models.Model):
    title = models.CharField(max_length = 50, null = True)
    def __str__(self):
        return self.title
    
class User_1(models.Model):
    
    name = models.CharField(max_length = 50, null = True)
    watch = models.ManyToManyField(Viedo, null = True)
    def __str__(self):
        return self.name
    
    

