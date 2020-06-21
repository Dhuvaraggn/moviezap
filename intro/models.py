from django.db import models

# Create your models here.
class moviezap(models.Model):
    year=models.IntegerField('year')
    genre=models.TextField('genre') 
    lang=models.TextField('lang')
    def __str__(self):
        return self.name
