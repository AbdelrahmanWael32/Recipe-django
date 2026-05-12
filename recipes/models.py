from django.db import models
from Accounts.models import Profile

class Recipe(models.Model):
    COURSE_CHOICES = [
        ("appetizer", "Appetizer"),
        ("main course", "Main Course"),
        ("dessert", "Dessert"),
    ]

    DIFFICULTY_CHOICES = [
        ("easy", "Easy"),
        ("medium", "Medium"),
        ("hard", "Hard"),
    ]

    name = models.CharField(max_length=255)
    course_type = models.CharField(max_length=50, choices=COURSE_CHOICES)
    difficulty = models.CharField(max_length=10, choices=DIFFICULTY_CHOICES)
    cooking_time = models.CharField(max_length=50)  
    recipe_img = models.URLField(max_length=500, blank=True)
    favourited_by = models.ManyToManyField(Profile, related_name="favourite_recipes", blank=True)

    def __str__(self):
        return self.name
    
class Ingredient(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name="ingredients")
    text = models.CharField(max_length=255) 

    def __str__(self):
        return f"{self.recipe.name} — {self.text}"


class Instruction(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name="instructions")
    step_number = models.PositiveIntegerField()
    text = models.TextField(max_length=255)

    class Meta:
        ordering = ["step_number"]

    def __str__(self):
        return f"{self.recipe.name} — Step {self.step_number}"