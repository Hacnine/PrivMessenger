from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'passmessage', 'password']

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance

    def validate_username(self, value):
        # Check if the username is unique
        if User.objects.filter(username=value).exists():
            raise serializers.ValidationError('Username must be unique.')
        return value
