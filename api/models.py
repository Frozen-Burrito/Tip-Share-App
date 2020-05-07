from django.db import models

# Create your models here.

class Tip (models.Model):

    author = models.CharField(max_length=30)
    body = models.CharField(max_length=200)

    def __str__ (self):
        return f"{self.author}'s life-changing tip"
