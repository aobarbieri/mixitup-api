from django.db import models
from django.core.validators import MinLengthValidator

# Create your models here.
# Make migrations after modifying this file
# python3 manage.py makemigrations
# python3 manage.py migrate
# To clear old records when migrating (only during development):
# python3 manage.py shell
# from projectFolderName.models import ModelName
# ClassName.objects.all().delete()
   
class Strength(models.Model):
    name = models.CharField(max_length=20)
    def __str__(self):
        return self.name
    
class Flavor(models.Model):
    name = models.CharField(max_length=20)
    def __str__(self):
        return self.name

class Ingredient(models.Model):
    name = models.CharField(max_length=30)
    def __str__(self):
        return self.name

class Drink(models.Model):
    name = models.CharField(max_length=30)
    date = models.DateField(auto_now=True)
    slug = models.SlugField(unique=True, null=True)
    
    strength = models.ForeignKey(Strength, null=True, on_delete=models.SET_NULL)
    flavors = models.ManyToManyField(Flavor, null=True)
    ingredients = models.ManyToManyField(Ingredient, null=True, through='DrinkIngredient')

class DrinkIngredient(models.Model):
    amount = models.DecimalField(max_digits=5, decimal_places=2)
    
    drink = models.ForeignKey(Drink, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)

class Instruction(models.Model):
    description = models.TextField(validators=[MinLengthValidator(10)])
    
    drink = models.ForeignKey(Drink, on_delete=models.CASCADE)