from rest_framework import serializers
from .models import ChatRoom, Message, Image, File
from account.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name', 'email']


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ['img']


class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = ['file']


class MessageSerializer(serializers.ModelSerializer):
    sender_details = UserSerializer(source='sender', read_only=True)
    images = ImageSerializer(many=True, read_only=True)
    files = FileSerializer(many=True, read_only=True)

    class Meta:
        model = Message
        fields = ['id', 'chatroom', 'sender', 'sender_details', 'message', 'created_at', 'updated_at', 'images', 'files']

    def create(self, validated_data):
        sender = validated_data.get('sender')
        chatroom = validated_data.get('chatroom')
        receiver_id = self.context['request'].data.get('receiver_id')

        if not chatroom and receiver_id:
            receiver = User.objects.get(id=receiver_id)
            chatroom = ChatRoom.objects.filter(participants=sender).filter(participants=receiver).first()

            if not chatroom:
                chatroom = ChatRoom.objects.create()
                chatroom.participants.add(sender, receiver)
                chatroom.save()

        validated_data['chatroom'] = chatroom  # Ensure chatroom is set in validated_data
        message = super().create(validated_data)
        return message


class ChatRoomSerializer(serializers.ModelSerializer):
    participants = UserSerializer(many=True, read_only=True)

    class Meta:
        model = ChatRoom
        fields = ['id', 'name', 'participants', 'created_at']

    def get_chatroom_name(self, obj):
        request_user = self.context.get('request').user
        return obj.get_chatroom_name_for_user(request_user)
