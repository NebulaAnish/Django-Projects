from django.db import models

# Create your models here.


class Listings(models.Model):
    title = models.CharField(max_length=150)
    price = models.IntegerField()
    num_of_bedrooms = models.IntegerField()
    num_of_bathrooms = models.IntegerField()
    area = models.IntegerField()
    address = models.CharField(max_length=100)
    image = models.ImageField()

    def __str__(self):
        return self.title
