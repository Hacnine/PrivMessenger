from rest_framework import serializers
from .models import Message, Group
from account.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name', 'email']


class MessageSerializer(serializers.ModelSerializer):
    user_details = UserSerializer(source='user', read_only=True)
    user = serializers.CharField(write_only=True)

    class Meta:
        model = Message
        fields = ['user_details', 'user', 'message', 'img', 'file', 'created_at', 'updated_at']

    def create(self, validated_data):
        user_identifier = validated_data.pop('user')
        try:
            # Try to get the user by email or username
            user = User.objects.get(email=user_identifier)
        except User.DoesNotExist:
            try:
                user = User.objects.get(username=user_identifier)
            except User.DoesNotExist:
                raise serializers.ValidationError("User not found")

        validated_data['user'] = user
        return super().create(validated_data)


class GroupSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()  # Use StringRelatedField for user
    group_name = serializers.CharField(max_length=150, allow_blank=False)  # Set allow_blank=False
    group_img = serializers.ImageField()

    class Meta:
        model = Group
        fields = '__all__'
