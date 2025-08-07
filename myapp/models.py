from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import timedelta



class Stuff(models.Model):
    stuff_id = models.AutoField(primary_key=True)
    stuff_name = models.CharField(max_length=30)
    stuff_description = models.TextField()
    photo = models.URLField()
    is_top = models.BooleanField(default=False)
    is_main = models.BooleanField(default=False)
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
    stuff = models.ForeignKey(Stuff, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    added_at = models.DateTimeField(null=True)