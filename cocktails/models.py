from django.db import models
from django.core.validators import MinLengthValidator

# Create your models here.
# Make migrations after modifying this file
# python3 manage.py makemigrations
# python3 manage.py migrate

class Drink(models.Model):
    name = models.CharField(max_length=20)
    date = models.DateField(auto_now=True)
    image_name = models.CharField(max_length=100, null=True)
    slug = models.SlugField(unique=True, null=True)

class Instruction(models.Model):
    description = models.TextField(validators=[MinLengthValidator(10)])
    drink = models.ForeignKey(Drink, on_delete=models.CASCADE)

class Ingredient(models.Model):
    name = models.CharField(max_length=30)
    amount = models.DecimalField(max_digits=4, decimal_places=2)
    drink = models.ForeignKey(Drink, on_delete=models.CASCADE)
    
class Strength(models.Model):
    name = models.CharField(max_length=20)

class Flavor(models.Model):
    name = models.CharField(max_length=20)
    
    
# To clear old records when migrating (only during development):
# python3 manage.py shell
# from projectFolderName.models import ModelName
# ClassName.objects.all().delete()