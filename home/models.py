from django.db import models

# Create your models here.
class Song(models.Model):
    name=models.CharField(max_length=100)
    movieTitle=models.CharField(max_length=100)
    year=models.CharField(max_length=10)
    genre=models.CharField(max_length=50)
    singer=models.CharField(max_length=100)
    download=models.URLField()
    musicDirector=models.CharField(max_length=100)




    def __str__(self):
        return self.name+','+self.movieTitle+','+self.year+','+self.genre+','+self.singer+','+self.musicDirector




    
class BusDetail(models.Model):
    busno=models.CharField(max_length=6,unique=True)
    drivername=models.CharField(max_length=20)
    driverno=models.CharField(max_length=10,unique=True)
    address=models.CharField(max_length=50)
    identitycard=models.CharField(max_length=8)


    def __str__(self):
        return self.busno+','+self.drivername+','+self.driverno+','+self.address+','+self.identitycard       
