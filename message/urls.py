from django.urls import path
from .views import *

urlpatterns = [
    path('get-or-create-chatroom/', GetOrCreateChatRoomView.as_view()),
    # Get Chatroom-wise message
    path('chatroom/<int:chatroom_id>/messages/', ChatRoomMessagesView.as_view(), name='chatroom-messages'),
    # Post a new message in a Chatroom
    path('chatroom/<int:chatroom_id>/send-message/', SendMessage.as_view(), name='send-message'),

    path('<int:pk>/', RetrieveMessage.as_view()),
    path('edit/<int:pk>/', UpdateMessage.as_view()),
    path('delete/<int:pk>/', DestroyMessage.as_view()),
]
