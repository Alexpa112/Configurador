
from django.db import models

class Article(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    tax = models.DecimalField(max_digits=5, decimal_places=2)
    unit = models.CharField(max_length=20)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class ArticleOption(models.Model):
    article = models.ForeignKey(Article, related_name='options', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)  # Ej: Color, Talla
    value = models.CharField(max_length=100)  # Ej: Rojo, L, XL

    def __str__(self):
        return f"{self.name}: {self.value} ({self.article.name})"