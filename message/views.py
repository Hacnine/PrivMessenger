from .custom_pagintaion import CustomPagination
from account.renderers import UserRenderer
from rest_framework.filters import SearchFilter

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .models import *
from .serializers import *
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView, ListAPIView, DestroyAPIView, RetrieveAPIView, UpdateAPIView
from rest_framework.response import Response
from rest_framework import status


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def get_or_create_chatroom(request):
    print('request', request)
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


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def chatroom_list(request):
    user = request.user
    # Fetch chatrooms where the user has sent at least one message
    chatrooms = ChatRoom.objects.filter(messages__sender=user).distinct()

    serializer = ChatRoomSerializer(chatrooms, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def chatroom_messages(request, chatroom_id):
    try:
        # Filter messages by chatroom_id and order by created_at
        messages = Message.objects.filter(chatroom_id=chatroom_id).order_by('created_at')
        # Serialize the data
        serializer = MessageSerializer(messages, many=True)

        # Return the serialized data as a response
        return Response(serializer.data, status=status.HTTP_200_OK)

    except Message.DoesNotExist:
        return Response({"detail": "Messages not found."}, status=status.HTTP_404_NOT_FOUND)


class SendMessage(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, chatroom_id=None):
        data = request.data.copy()
        sender = request.user

        # If chatroom_id is provided in the URL, add it to the request data
        if chatroom_id:
            data['chatroom'] = chatroom_id

        data['sender'] = sender.id  # Set the sender in the data

        serializer = MessageSerializer(data=data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UpdateMessage(UpdateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = [IsAuthenticated]


class DestroyMessage(DestroyAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = [IsAuthenticated]


class CreateMessage(CreateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        sender = self.request.user
        serializer.save(sender=sender)


class MessageList(ListAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    # pagination_class = CustomPagination
    permission_classes = [IsAuthenticated]


class RetrieveMessage(RetrieveAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = [IsAuthenticated]
