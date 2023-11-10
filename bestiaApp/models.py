from django.db import models
from django.contrib.auth.models import User

# Model export to database
class bestia(models.Model):
    name = models.CharField( max_length=15)
    cultura = models.CharField( max_length=15)
    descripcion = models.CharField( max_length=15)
    image = models.ImageField(upload_to='media/', blank=True, null=True)
    
    def __str__(self):
        return self.name