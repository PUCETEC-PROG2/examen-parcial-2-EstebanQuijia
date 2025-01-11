from django.db import models

# Create your models here.

class Movie(models.Model):
    title = models.CharField(max_length=20) 
    genre = models.CharField(max_length=15) 
    director = models.CharField(max_length=12) 
    release_year = models.IntegerField() 
    synopsis = models.TextField() 
    def __str__(self):
        return f"{self.title} - {self.release_year}"