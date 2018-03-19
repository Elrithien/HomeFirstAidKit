from django.db import models

# Create your models here.

class Brand(models.Model):
    name = models.CharField(unique=True, max_length=500)


class Category(models.Model):
    name = models.CharField(unique=True, max_length=500)


class Type(models.Model):
    name = models.CharField(unique=True, max_length=500)


class Medicine(models.Model):
    name  = models.CharField(max_length=500)
    category = models.ForeignKey(Category)
    type = models.ForeignKey(Type)
    brand = models.ForeignKey(Brand)
    quantity = models.CharField(max_length=500)
    date = models.DateField()
    description = models.CharField(max_length=1500)
    link = models.CharField(max_length=500)


class Bandage(models.Model):
    name = models.CharField(max_length=500)
    brand = models.ForeignKey(Brand)
    quantity = models.IntegerField()
    date = models.DateField()
    description = models.CharField(max_length=1500)
    link = models.CharField(max_length=500)
