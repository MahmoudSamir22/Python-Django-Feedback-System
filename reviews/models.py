from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

class Review(models.Model):
    user_name = models.CharField(max_length=100)
    review_text = models.TextField(max_length=300)
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])