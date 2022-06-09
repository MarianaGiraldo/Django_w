from django.db import models

class Route(models.Model):
    id = models.AutoField(primary_key = True)
    origin = models.CharField( max_length = 255 )
    destination = models.CharField( max_length = 255 )
    
    def __str__(self):
        return f'{self.origin} -> {self.destination}'
