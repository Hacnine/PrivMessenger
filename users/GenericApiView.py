from rest_framework.renderers import JSONRenderer

from .custom_pagintaion import CustomPagination
from .models import *
from .serializers import *
from rest_framework.generics import CreateAPIView, ListAPIView, DestroyAPIView, RetrieveAPIView, UpdateAPIView

from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, \
    DestroyModelMixin
from rest_framework.filters import SearchFilter
from account.renderers import UserRenderer
from rest_framework.permissions import IsAuthenticated


class CreateMessage(CreateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = [IsAuthenticated]
    renderer_classes = [JSONRenderer]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class MessageList(ListAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    pagination_class = CustomPagination
    permission_classes = [IsAuthenticated]
    renderer_classes = [JSONRenderer]


class RetrieveMessage(RetrieveAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = [IsAuthenticated]
    renderer_classes = [JSONRenderer]


class UpdateMessage(UpdateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = [IsAuthenticated]
    renderer_classes = [JSONRenderer]


class DestroyMessage(DestroyAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = [IsAuthenticated]
    renderer_classes = [JSONRenderer]