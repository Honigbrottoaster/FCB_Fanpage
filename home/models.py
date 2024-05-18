from django.db import models

# Create your models here.
class ReviewEntery(models.Model):
    id = models.AutoField(primary_key=True)
    headline = models.CharField(max_length=200, null=False)
    description = models.CharField(max_length=1100, null=False)
    date = models.DateField()
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.headline

class GalerieImage(models.Model):
    id = models.AutoField(primary_key=True)
    image = models.ImageField(null=False, blank=False)

class PassWord(models.Model):
    text = models.CharField(null=False, blank=False, max_length=15)