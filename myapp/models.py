from django.db import models

class MyModel(models.Model):
    name = models.CharField(max_length=25, unique=True,)
