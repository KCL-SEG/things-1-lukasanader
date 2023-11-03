from django.db import models
import django.core.validators

# Create your models here.
class Thing(models):
    name= models.CharField(unique=True,max_length=30,blank=False)
    description = models.TextField(max_length=120,blank=True)
    quantity = models.IntegerField(
        validators=[
            django.core.validators.MinValueValidator(0),
            django.core.validators.MaxValueValidator(100)
        ]
    )