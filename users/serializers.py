from rest_framework import serializers
from .models import *


# class MessageSerializer(serializers.Serializer):
#     user = serializers.StringRelatedField()  # Use StringRelatedField for user
#     message = models.CharField(max_length=2000,  null=True, blank=True)
#     img = models.ImageField(null=True, blank=True)
#     file = models.FileField(null=True, blank=True)
#
#     def to_representation(self, instance):
#         data = super().to_representation(instance)
#         return data
#
#     def create(self, validated_data):
#         return Message.objects.create(**validated_data)

class MessageSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = Message
        fields = '__all__'
        read_only_fields = ['id', 'user']
 
    # def create(self, validated_data):
    #     return Message.objects.create(**validated_data)

    # def update(self, instance, validated_data):
    #     instance.message = validated_data.get('message', instance.message)
    #
    #     if 'img' in validated_data:
    #         instance.img = validated_data['img']
    #
    #     if 'file' in validated_data:
    #         instance.file = validated_data['file']
    #
    #     instance.save()
    #     return instance


class GroupSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()  # Use StringRelatedField for user
    group_name = serializers.CharField(max_length=150, allow_blank=False)  # Set allow_blank=False
    group_img = serializers.ImageField()

    class Meta:
        model = Group
        fields = '__all__'
