from django.db import models
from django.contrib.auth.models import User

class Category(models.TextChoices):
    PHONE = 'phone', 'Phone'
    VOITURE = 'voiture', 'Voiture'

class Ville(models.TextChoices):
    CASABLANCA = 'casablanca', 'Casablanca'
    RABAT = 'rabat', 'Rabat'

class Article(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    photo1 = models.ImageField(upload_to='photos/')
    photo2 = models.ImageField(upload_to='photos/')
    photo3 = models.ImageField(upload_to='photos/')
    phone_number = models.CharField(max_length=15)
    category = models.CharField(max_length=40, choices=Category.choices)
    ville = models.CharField(max_length=40, choices=Ville.choices)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='articles')

    def __str__(self):
        return self.name
