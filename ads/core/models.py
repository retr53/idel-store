from django.db import models

# Create your models here.
class Moto:
    name = models.CharField(max_length=100)
    price = models.IntegerField(default=0)
    description = models.TextField()
    
    

    def __str__(self):
        return self.name

