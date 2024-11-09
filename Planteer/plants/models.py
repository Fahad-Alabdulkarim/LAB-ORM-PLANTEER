from django.db import models

# Create your models here.

class Plant(models.Model):
    class CategoryChoices(models.TextChoices):
        TREE = 'Tree'
        FRUIT = 'Fruit'
        VEGETABLE = 'Vegetable'
        FLOWER = 'Flower'

    name = models.CharField(max_length=100)
    about = models.TextField()
    used_for = models.TextField()
    image = models.ImageField(upload_to='plants/')
    category = models.CharField(max_length=50, choices=CategoryChoices.choices)
    is_edible = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
