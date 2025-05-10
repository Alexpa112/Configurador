from rest_framework import serializers
from .models import Article, ArticleOption

class ArticleOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArticleOption
        fields = ['id', 'name', 'value']

class ArticleSerializer(serializers.ModelSerializer):
    options = ArticleOptionSerializer(many=True, read_only=True)

    class Meta:
        model = Article
        fields = ['id', 'name', 'category', 'price', 'tax', 'unit', 'active', 'options']