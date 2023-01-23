from django.db import models

# Create your models here.

class Listing(models.Model):
   title = models.CharField(max_length=200)
   author = models.CharField(max_length=100)
   price = models.FloatField()
   ratings = models.FloatField()
   image = models.ImageField()
   def __str__(self):
      return self.title