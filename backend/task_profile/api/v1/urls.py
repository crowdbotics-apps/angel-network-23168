from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import (
    CustomerProfileViewSet,
    InviteCodeViewSet,
    NotificationViewSet,
    TaskerProfileViewSet,
)

router = DefaultRouter()
router.register("customerprofile", CustomerProfileViewSet)
router.register("notification", NotificationViewSet)
router.register("invitecode", InviteCodeViewSet)
router.register("taskerprofile", TaskerProfileViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
