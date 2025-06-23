from django.db import models
from django.contrib.auth.models import User




class administration(models.Model):
    id = models.IntegerField(primary_key=True)
    login = models.CharField(max_length=25, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=20)





class product(models.Model):
    id = models.AutoField(primary_key=True)
    product_name = models.CharField(blank=False, max_length=80)
    product_price = models.IntegerField(blank=False)
    product_description = models.TextField(blank=False)



class cart(models.Model):
    id = models.IntegerField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    added_at = models.DateTimeField(null=True)