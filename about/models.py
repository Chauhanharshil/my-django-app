from django.db import models

# Create your models here.
class photos(models.Model):
    name = models.CharField(max_length= 10,null=True)
    about_photo = models.ImageField(upload_to='images')