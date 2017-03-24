from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company = models.ForeignKey('Company')
    active = models.BooleanField()


class Company(models.Model):
    name = models.CharField(max_length=64)
    street1 = models.TextField(max_length=64)
    street2 = models.TextField(max_length=64)
    city = models.TextField(max_length=64)
    state = models.TextField(max_length=64)
    zip = models.TextField(max_length=12)
    active = models.BooleanField()


class Order(models.Model):
    user = models.ForeignKey(User)
    company = models.ForeignKey('Company')
    grandTotal = models.FloatField()
    payment_receipt = models.TextField()


class Item(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField()
    category = models.CharField(max_length=64)
    picture = models.CharField(max_length=64)
    weight = models.FloatField()
    inventory_level = models.IntegerField()
    reorder_level = models.IntegerField()
    active = models.BooleanField()


class OrderItem(models.Model):
    order = models.ForeignKey('Order')
    item = models.ForeignKey('Item')
    quantity = models.IntegerField()
    shipped_on = models.DateTimeField(auto_now_add=True)


class ItemPrice(models.Model):
    item = models.ForeignKey('Item')
    price = models.FloatField()
    category = models.CharField()
    start_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField()


class Purchase(models.Model):
    item = models.ForeignKey('Item')
    quantity = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)

