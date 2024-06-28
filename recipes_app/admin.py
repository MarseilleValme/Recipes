from django.contrib import admin
from .models import RecipeCategory, Recipe


class RecipeAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']


admin.site.register(RecipeCategory)
admin.site.register(Recipe, RecipeAdmin)
