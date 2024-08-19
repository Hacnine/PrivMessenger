from rest_framework.views import APIView
from .custom_pagintaion import CustomPagination
from .models import *
from .serializers import *
from rest_framework.generics import CreateAPIView, ListAPIView, DestroyAPIView, RetrieveAPIView, UpdateAPIView
from rest_framework.filters import SearchFilter
from account.renderers import UserRenderer
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


class GetOrCreateChatRoomView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        user1 = request.user
        user2_id = request.data.get('user2_id')

        try:
            user2 = User.objects.get(id=user2_id)
        except User.DoesNotExist:
            return Response({"error": "User not found"}, status=404)

        # Check if a chatroom already exists between these two users
        chatroom = ChatRoom.objects.filter(participants=user1).filter(participants=user2).first()

        if not chatroom:
            # If no chatroom exists, create a new one
            chatroom = ChatRoom.objects.create()
            chatroom.participants.add(user1, user2)
            chatroom.save()

        serializer = ChatRoomSerializer(chatroom)
        return Response(serializer.data)


class CreateMessage(CreateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        sender = self.request.user
        receiver_id = self.request.data.get('receiver_id')
        receiver = User.objects.get(id=receiver_id)

        # Check if a chat room already exists between the two users
        chatroom = ChatRoom.objects.filter(participants=sender).filter(participants=receiver).first()

        if not chatroom:
            # Create a new chat room
            chatroom = ChatRoom.objects.create()
            chatroom.participants.add(sender, receiver)
            chatroom.save()

        serializer.save(chatroom=chatroom, sender=sender)


class MessageList(ListAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    # pagination_class = CustomPagination
    permission_classes = [IsAuthenticated]


class RetrieveMessage(RetrieveAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = [IsAuthenticated]


class UpdateMessage(UpdateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = [IsAuthenticated]


class DestroyMessage(DestroyAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = [IsAuthenticated]
