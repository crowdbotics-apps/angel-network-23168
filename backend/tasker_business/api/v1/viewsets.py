from rest_framework import authentication
from tasker_business.models import (
    BusinessPhoto,
    TaskerAvailability,
    TaskerSkill,
    Timeslot,
)
from .serializers import (
    BusinessPhotoSerializer,
    TaskerAvailabilitySerializer,
    TaskerSkillSerializer,
    TimeslotSerializer,
)
from rest_framework import viewsets


class TaskerAvailabilityViewSet(viewsets.ModelViewSet):
    serializer_class = TaskerAvailabilitySerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = TaskerAvailability.objects.all()


class BusinessPhotoViewSet(viewsets.ModelViewSet):
    serializer_class = BusinessPhotoSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = BusinessPhoto.objects.all()


class TimeslotViewSet(viewsets.ModelViewSet):
    serializer_class = TimeslotSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = Timeslot.objects.all()


class TaskerSkillViewSet(viewsets.ModelViewSet):
    serializer_class = TaskerSkillSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = TaskerSkill.objects.all()
