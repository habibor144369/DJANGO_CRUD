from django.db import models

# Create your models here.
class Musician(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    instrument = models.CharField(max_length=100)
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
        # return f"{self.first_name +' '+ self.last_name}" there are same...



class Album(models.Model):
    artist = models.ForeignKey(Musician, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    release_date = models.DateField()
    rating = (
        (1, "Worst"),
        (2, "Bad"),
        (3, "Not Bad"),
        (4, "Good"),
        (5, "Excelent!"),
    )
    num_stars = models.IntegerField(choices=rating)
   
    def __str__(self):
        return f"{self.name + ' Rating - ' + str(self.num_stars)}"
