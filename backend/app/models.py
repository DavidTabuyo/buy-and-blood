from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    auth_provider = models.CharField(max_length=255)
    plan = models.ForeignKey('Plan', on_delete=models.SET_NULL, null=True, blank=True)

class Asset(models.Model):
    symbol = models.CharField(max_length=50, unique=True)
    name = models.CharField(max_length=255, unique=True)
    TYPE_CHOICES = [
        ('stock', 'Stock'),
        ('crypto', 'Crypto'),
    ]
    type = models.CharField(max_length=10, choices=TYPE_CHOICES)

class Transaction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    asset = models.ForeignKey(Asset, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=20, decimal_places=8)
    amount = models.DecimalField(max_digits=20, decimal_places=8)
    datetime = models.DateTimeField(auto_now_add=True)

class Holding(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    asset = models.ForeignKey(Asset, on_delete=models.CASCADE)
    mean_price = models.DecimalField(max_digits=20, decimal_places=8)
    amount = models.DecimalField(max_digits=20, decimal_places=8)

class Plan(models.Model):
    name = models.CharField(max_length=255, unique=True)

class PlanAsset(models.Model):
    plan = models.ForeignKey(Plan, on_delete=models.CASCADE)
    asset = models.ForeignKey(Asset, on_delete=models.CASCADE)
    percentage = models.DecimalField(max_digits=5, decimal_places=2)

    class Meta:
        unique_together = ('plan', 'asset')
