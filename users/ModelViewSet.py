from rest_framework.authentication import BasicAuthentication, SessionAuthentication
from rest_framework.permissions import (IsAuthenticated, AllowAny, IsAdminUser, IsAuthenticatedOrReadOnly,
                                        DjangoModelPermissions,
                                        DjangoModelPermissionsOrAnonReadOnly)
from .models import *
from .serializers import *
from rest_framework import viewsets
from .custom_permission import MyPermission


class MessageModelViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [MyPermission]


class MessageReadOnlyModelViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer


# Ignoring global authentication
class MessageModelViewSetForALL(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [AllowAny]
