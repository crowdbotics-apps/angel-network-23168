from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import CategoryViewSet, SubcategoryViewSet

router = DefaultRouter()
router.register("category", CategoryViewSet)
router.register("subcategory", SubcategoryViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
