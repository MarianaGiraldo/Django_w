from django.db import models

class Passenger(models.Model):
    id = models.AutoField(primary_key = True)
    full_name = models.CharField( max_length = 255 )
    document = models.CharField( max_length = 11 )
    email = models.EmailField( max_length = 255 )
    phone = models.CharField( max_length = 11 )
    password = models.CharField( max_length = 255 )
    
    def __str__(self):
        return self.full_name
