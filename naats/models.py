from django.db import models
from djrichtextfield.models import RichTextField


class Naat(models.Model):
    tittle = models.CharField(max_length=100)
    lyrics = models.TextField()


    def __str__(self):
        return self.tittle
    



