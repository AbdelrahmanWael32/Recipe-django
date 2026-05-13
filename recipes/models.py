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
    
    @staticmethod
    def create_recipe(recipe_name, course_type, selected_difficulty, cooking_time, recipe_img, ingredients, instructions):
        recipe = Recipe.objects.create(
            name=recipe_name,
            course_type=course_type,
            cooking_time=cooking_time,
            difficulty=selected_difficulty,
            recipe_img=recipe_img
        )

        for ingredient in ingredients:
            Ingredient.objects.create(recipe=recipe, text=ingredient)

        for i, instruction_text in enumerate(instructions, start=1):
            Instruction.objects.create(recipe=recipe, step_number = i, text=instruction_text)
        return recipe
    
    @staticmethod
    def update_recipe(recipe_id, recipe_name, course_type, selected_difficulty, cooking_time, recipe_img, ingredients, instructions):
        recipe = Recipe.objects.get(id=recipe_id)
        recipe.name = recipe_name
        recipe.course_type = course_type
        recipe.difficulty = selected_difficulty
        recipe.cooking_time = cooking_time
        recipe.recipe_img = recipe_img
        recipe.save()

        recipe.ingredients.all().delete()
        recipe.instructions.all().delete()

        for ingredient in ingredients:
            if ingredient.strip():
                Ingredient.objects.create(recipe=recipe, text=ingredient.strip())

        for i, instruction_text in enumerate(instructions, start=1):
            if instruction_text.strip():
                Instruction.objects.create(recipe=recipe, step_number=i, text=instruction_text.strip())

        return recipe

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