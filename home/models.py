from django.db import models

# Create your models here.
class Harsh(models.Model):
    harsh_image = models.ImageField(upload_to='images')