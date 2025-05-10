from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ArticleViewSet, ArticleOptionViewSet

router = DefaultRouter()
router.register(r'articles', ArticleViewSet)
router.register(r'options', ArticleOptionViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
