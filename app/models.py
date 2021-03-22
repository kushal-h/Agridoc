from django.db import models

# Create your models here.

class Predictions(models.Model):
    image_path = models.CharField(max_length=200)
    prediction = models.CharField(max_length=200)

class ImagePath:
    path: str