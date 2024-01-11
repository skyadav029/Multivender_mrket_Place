from django.db import models

# Create your models here.
class Product(models.Model):
    name =models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    price= models.FloatField(default=0)
    file= models.FileField(upload_to='uploads')

    def __self__(self):
        return self.name
