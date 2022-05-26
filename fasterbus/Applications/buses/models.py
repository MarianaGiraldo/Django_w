from django.db import models

class Bus(models.Model):
    id = models.AutoField(primary_key = True)
    plate = models.CharField( max_length = 7 )
    type = models.CharField( max_length = 255 )
    capacity = models.SmallIntegerField()
    company = models.CharField( max_length = 255 )
   