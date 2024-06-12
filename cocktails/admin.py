from django.contrib import admin
from .models import Strength, Flavor, Ingredient, Drink, DrinkIngredient, Instruction

# Register your models here.
class StrengthAdmin(admin.ModelAdmin):
    pass


class FlavorAdmin(admin.ModelAdmin):
    pass


class IngredientAdmin(admin.ModelAdmin):
    pass


class DrinkAdmin(admin.ModelAdmin):
    pass

class DrinkIngredientAdmin(admin.ModelAdmin):
    pass

class InstructionAdmin(admin.ModelAdmin):
    pass


admin.site.register(Strength, StrengthAdmin)
admin.site.register(Flavor, FlavorAdmin)
admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(Drink, DrinkAdmin)
admin.site.register(DrinkIngredient, DrinkIngredientAdmin)
admin.site.register(Instruction, InstructionAdmin)
