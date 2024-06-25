from rest_framework import viewsets
from rest_framework.response import Response

from .models import *
from .serializers import *
from django.shortcuts import render
from rest_framework import status
from rest_framework import viewsets


class MessageViewSet(viewsets.ViewSet):
    def list(self, request):
        message = Message.objects.all()
        serializer = MessageSerializer(message, many=True)
        return Response(serializer.data)

    def retrive(self, request, pk=None):
        id = pk
        if id is not None:
            message = Message.objects.get(id=id)
            serializer = MessageSerializer(message)
            return Response(serializer.data)

    def create(self, request):
        serializer = MessageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Data Created'}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk):
        id = pk
        stu = Message.objects.get(pk=id)
        serializer = MessageSerializer(stu, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Complete Data Updated'})

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, pk):
        id = pk
        stu = Message.objects.get(pk=id)
        serializer = MessageSerializer(stu, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Partial Data Updated'})

        return Response(serializer.errors)

    def destroy(self, request, pk):
        id = pk
        message = Message.objects.get(pk=id)
        message.delete()
        return Response({'msg': 'Data Deleted'})
