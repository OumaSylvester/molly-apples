from django.db import models
from django.urls import reverse

class Apple(models.Model):
    year_of_production = models.IntegerField()
    breed = models.CharField(max_length=100)
    row = models.IntegerField()
    column = models.IntegerField()
    geolocation = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.breed

    def get_absolute_url(self):
        return reverse('apple_register', {'pk': self.pk})

