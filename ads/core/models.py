from django.db import models

# Create your models here.
class Moto(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField(default=0)
    description = models.TextField()
    image = models.ImageField(upload_to="core/image/",null=True, blank=True)
    
    

    def __str__(self):
        return self.name

