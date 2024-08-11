from rest_framework import serializers
from .models import *
from account.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name', 'email']


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ['img']


class MessageSerializer(serializers.ModelSerializer):
    user_details = UserSerializer(source='user', read_only=True)
    user = serializers.CharField(write_only=True)
    img = ImageSerializer(many=True, required=False, source='images')

    class Meta:
        model = Message
        fields = ['user_details', 'user', 'message', 'img', 'file', 'created_at', 'updated_at']

    def create(self, validated_data):
        user_identifier = validated_data.pop('user')
        img_data = self.context['request'].FILES.getlist('img')  # Use request.FILES.getlist to retrieve the images
        try:
            user = User.objects.get(email=user_identifier)
        except User.DoesNotExist:
            raise serializers.ValidationError("User not found")

        message = Message.objects.create(user=user, **validated_data)

        for img in img_data:
            Image.objects.create(message=message, img=img)

        return message


class GroupSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()  # Use StringRelatedField for user
    group_name = serializers.CharField(max_length=150, allow_blank=False)  # Set allow_blank=False
    group_img = serializers.ImageField()

    class Meta:
        model = Group
        fields = '__all__'
