from django.db import models
from ckeditor.fields import RichTextField

class Naat(models.Model):
    tittle = models.CharField(max_length=100)
    lyrics = RichTextField()

    def __str__(self):
        return self.tittle
    



