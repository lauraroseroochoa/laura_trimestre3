from django.db import models

# Create your models here.
class Usuario(models.Model):
    nombre = models.CharField(max_length=50)
    docuemento = models.IntegerField()
    ficha=models.IntegerField()
    photo = models.ImageField(upload_to='photo_user')