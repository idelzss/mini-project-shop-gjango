from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import timedelta



class Stuff(models.Model):
    stuff_id = models.AutoField(primary_key=True)
    stuff_name = models.CharField(max_length=30, blank=True)
    stuff_description = models.TextField(blank=True)
    photo = models.URLField(blank=True)
    is_top = models.BooleanField(default=False)
    is_main = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    price = models.FloatField(blank=True, null=True)
    rate = models.PositiveIntegerField(default=0, validators=[MinValueValidator(1), MaxValueValidator(10)], blank=True, null=True)


    def is_still_new(self):
        return timezone.now() - self.created_at < timedelta(days=3)


    def __str__(self):
        return self.stuff_name




class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="cart")
    created_at = models.DateTimeField(auto_now_add=True)

    def total_price(self):
        return sum(item.total_price() for item in self.items.all())

    def __str__(self):
        return f"Cart of {self.user.username}"


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, related_name="items", on_delete=models.CASCADE)
    stuff = models.ForeignKey(Stuff, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    added_at = models.DateTimeField(auto_now_add=True)

    def total_price(self):
        return self.stuff.price * self.quantity

    def __str__(self):
        return f"{self.stuff.stuff_name} ({self.quantity})"