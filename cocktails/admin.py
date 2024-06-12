from django.contrib import admin
from .models import Strength, Flavor, Ingredient, Drink, DrinkIngredient, Instruction

# Register your models here.

# Inline admin classes for related models
class DrinkIngredientInline(admin.TabularInline):
    model = DrinkIngredient
    extra = 0
    
class InstructionInLine(admin.TabularInline):
    model = Instruction
    extra = 0

# ModelAdmin classes for each model
class StrengthAdmin(admin.ModelAdmin):
    list_display = ('name',)

class FlavorAdmin(admin.ModelAdmin):
    list_display = ('name',)

class IngredientAdmin(admin.ModelAdmin):
    list_display = ('name',)
    
class DrinkAdmin(admin.ModelAdmin):
    list_display = ('name', 'strength_name', 'flavors_list', 'ingredients_list', 'instructions_count')

    def strength_name(self, obj):
        return obj.strength.name if obj.strength else '-'
    
    def flavors_list(self, obj):
        return ', '.join([flavor.name for flavor in obj.flavors.all()]) 
    
    def ingredients_list(self, obj):
        return ', '.join([ingredient.name for ingredient in obj.ingredients.all()])
    
    def instructions_count(self, obj):
        return obj.instruction_set.count()

    inlines = [DrinkIngredientInline, InstructionInLine]


admin.site.register(Strength, StrengthAdmin)
admin.site.register(Flavor, FlavorAdmin)
admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(Drink, DrinkAdmin)
