from django.db import models


class ParseData(models.Model):
    title = models.CharField(max_length=255)
    price = models.PositiveIntegerField()
    image = models.ImageField()
    link = models.ForeignKey('Link', on_delete=models.CASCADE)


class Link(models.Model):
    link = models.URLField()

