from django.db import models


# Create your models here.
class Female(models.Model):
    female_name = models.CharField(max_length=50, null = True)
    def __str__(self):
        return self.female_name

class Male (models.Model):
    male_name = models.CharField(max_length=50, null = True)
    options = models.OneToOneField(Female ,on_delete = models.CASCADE)
    def __str__(self):
        return self.male_name
      

class Product (models.Model):
    title = models.CharField(max_length=50, null=True)
    def __str__(self):
        return self.title

class User (models.Model):
    products = models.ForeignKey(Product, on_delete= models.CASCADE)

    name = models.CharField(max_length=50, null=True)
    def __str__(self):
        return self.name
    


class Vedio (models.Model):
    title = models.CharField(max_length=50, null=True)
    def __str__(self):
        return self.title

class User_1 (models.Model):

    watch = models.ManyToManyField(Vedio,)
    name = models.CharField(max_length=50, null=True)
    def __str__(self):
        return self.name
    

class Login (models.Model):
        user_name = models.CharField(max_length = 15)
        passw = models.CharField(max_length = 15, )
