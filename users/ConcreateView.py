from .models import *
from .serializers import *
from rest_framework.generics import (ListAPIView, ListCreateAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView,
                                     RetrieveUpdateDestroyAPIView,
                                     DestroyAPIView)


class MessageList(ListAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer


class CreateMessage(CreateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer


class ListCreateMessage(ListCreateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer


class RetrieveMessage(RetrieveAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer


class UpdateMessage(UpdateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer


class DestroyMessage(DestroyAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer


class RetrieveUpdateDestroyMessage(RetrieveUpdateDestroyAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
