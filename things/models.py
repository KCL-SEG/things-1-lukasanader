from django.db import models

# Create your models here.
class Thing():
    name= models.CharField(unique=True,max_length=30,blank=False)
    description = models.TextField(max_length=120,blank=True)
    quantity = models.IntegerField(
        validators=[
            max(100),
            min(0)
        ],
        blank=True
    )