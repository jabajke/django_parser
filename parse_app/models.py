from django.db import models
from django.contrib.auth.models import User


class ParseData(models.Model):
    title = models.CharField(max_length=255)
    price = models.FloatField()
    image = models.ImageField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

