from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=20)
    phone = models.CharField(max_length=15, blank=True, unique=True)

    def publish(self):
        self.save()

class Product(models.Model):
    product_name = models.CharField(max_length=100)
    product_description = models.TextField()
    product_price = models.IntegerField()
