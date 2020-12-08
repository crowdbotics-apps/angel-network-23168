from rest_framework import authentication
from task.models import Message, Rating, Task, TaskTransaction
from .serializers import (
    MessageSerializer,
    RatingSerializer,
    TaskSerializer,
    TaskTransactionSerializer,
)
from rest_framework import viewsets


class RatingViewSet(viewsets.ModelViewSet):
    serializer_class = RatingSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = Rating.objects.all()


class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = Task.objects.all()


class TaskTransactionViewSet(viewsets.ModelViewSet):
    serializer_class = TaskTransactionSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = TaskTransaction.objects.all()


class MessageViewSet(viewsets.ModelViewSet):
    serializer_class = MessageSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = Message.objects.all()
