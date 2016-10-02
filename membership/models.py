from django.db import models

# Create your models here.
class membershiptype(models.Model):
    type = models.CharField(max_length=200)
    price = models.IntegerField()
