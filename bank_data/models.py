"""Models."""
from django.db import models


class Bank(models.Model):
    """Bank."""

    name = models.CharField(max_length=49)
    id = models.IntegerField(primary_key=True)


class Branch(models.Model):
    """Branch."""

    ifsc = models.CharField(max_length=11, primary_key=True)
    bank_id = models.ForeignKey(Bank, on_delete=models.CASCADE)
    branch = models.CharField(max_length=150)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=50)
    district = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
