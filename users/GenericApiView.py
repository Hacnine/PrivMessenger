from .models import *
from .serializers import *
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin
from django_filters.rest_framework import DjangoFilterBackend


class MessageList(GenericAPIView, ListModelMixin):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['message']
    #   http://127.0.0.1:8000/msg/all/?message=As%20Salam
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class CreateMessage(GenericAPIView, CreateModelMixin):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class RetrieveMessage(GenericAPIView, RetrieveModelMixin):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


class UpdateMessage(GenericAPIView, RetrieveModelMixin):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)


class DestroyMessage(GenericAPIView, DestroyModelMixin):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)