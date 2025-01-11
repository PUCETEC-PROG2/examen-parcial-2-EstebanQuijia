from django.db import models

# Create your models here.

class Movie(models.Model):
    title = models.CharField(max_length=20, null=False) 
    genre = models.CharField(max_length=10, null=False) 
    director = models.CharField(max_length=20) 
    year = models.IntegerField() 
    synopsis = models.TextField() 
    
    def __str__(self):
        return f"{self.title} - {self.year}"