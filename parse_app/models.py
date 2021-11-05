from django.db import models


class ParseData(models.Model):
    title = models.CharField(max_length=255)
    price = models.FloatField()
    image = models.ImageField()
    category = models.CharField(max_length=255)
