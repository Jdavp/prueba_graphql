from django.db import models

# Create your models here.

class Planet(models.Model):
    name = models.CharField(max_length=30)
    
    def __str__(self):
        return self.name

class Film(models.Model):
    film_title = models.CharField(max_length=100)
    director = models.CharField(max_length=100)
    producer = models.CharField(max_length=100)
    opening_crawl = models.CharField(max_length=1000)
    planets = models.ManyToManyField(Planet, related_name='planet')

    def __str__(self):
        return self.film_title

class Character(models.Model):
    name = models.CharField(max_length=100)
    films = models.ManyToManyField(Film, related_name='film')

    def __str__(self):
        return self.name







