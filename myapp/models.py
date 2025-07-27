from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import timedelta



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


class Stuff(models.Model):
    stuff_id = models.AutoField(primary_key=True)
    stuff_name = models.CharField(max_length=30)
    stuff_description = models.TextField()
    photo = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)
    price = models.FloatField()
    rate = models.PositiveIntegerField(default=0, validators=[MinValueValidator(1), MaxValueValidator(10)])


    def is_still_new(self):
        return timezone.now() - self.created_at < timedelta(days=3)


    def __str__(self):
        return self.stuff_name



class cart(models.Model):
    id = models.IntegerField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    added_at = models.DateTimeField(null=True)