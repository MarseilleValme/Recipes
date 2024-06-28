from django.db import models
from django.contrib.auth.models import User


class Recipe(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    cooking_steps = models.TextField()
    preparation_time = models.PositiveIntegerField()
    image = models.ImageField(upload_to='images/')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='recipes')


    def __str__(self):
        return self.name


class RecipeCategory(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class RecipeCategoryRelationship(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    category = models.ForeignKey(RecipeCategory, on_delete=models.CASCADE)

    class Meta:
        unique_together = ['recipe', 'category']  