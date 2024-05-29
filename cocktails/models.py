from django.db import models
from django.core.validators import MinLengthValidator

# Create your models here.
# Make migrations after modifying this file
# python3 manage.py makemigrations

class Drink(models.Model):
    name = models.CharField(max_length=20)
    date = models.DateField(auto_now=True)
    image_name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    
class Ingredient(models.Model):
    name = models.CharField(max_length=30)
    amount = models.FloatField()
    
class Instruction(models.Model):
    description = models.TextField(validators=[MinLengthValidator(10)])
    
class Strength(models.Model):
    name = models.CharField(max_length=20)

class Flavor(models.Model):
    name = models.CharField(max_length=20)