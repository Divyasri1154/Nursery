from django.db import models

class Plant(models.Model):
    scientific_name=models.TextField(max_length=100)
    price= models.IntegerField(default=100)
    age=models.IntegerField(default=1)
    pic=models.ImageField(null=True)
    imported = models.BooleanField(default=False)