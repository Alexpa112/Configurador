from rest_framework import viewsets
from .models import Article, ArticleOption
from .serializers import ArticleSerializer, ArticleOptionSerializer

class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

class ArticleOptionViewSet(viewsets.ModelViewSet):
    queryset = ArticleOption.objects.all()
    serializer_class = ArticleOptionSerializer
