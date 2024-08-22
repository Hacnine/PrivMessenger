from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from . import views
from .GenericApiView import *
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

urlpatterns = [
    path('get-or-create-chatroom/', GetOrCreateChatRoomView.as_view()),
    # Fetch all messages in a specific chatroom
    path('chatroom/<int:chatroom_id>/messages/', ChatRoomMessagesView.as_view(), name='chatroom-messages'),

    # Post a new message
    path('chatroom/<int:chatroom_id>/send-message/', SendMessage.as_view(), name='send-message'),

    path('post/', CreateMessage.as_view()),
    path('all/', MessageList.as_view()),
    path('<int:pk>/', RetrieveMessage.as_view()),
    path('edit/<int:pk>/', UpdateMessage.as_view()),
    path('delete/<int:pk>/', DestroyMessage.as_view()),
]

''' For ModelView Set '''
# # Creating Router Objects
# router = DefaultRouter()
#
# # Register StudentViewSet with Router
# router.register('message', ModelViewSet.MessageModelViewSet, basename='message')
# # router.register('read_only_message', ModelViewSet.MessageReadOnlyModelViewSet, basename='model_view_set_message')
#
# urlpatterns = [
#     path('all/', include(router.urls)),
#     # path('allreadonly/', include(router.urls)),
#
# ]

''' For View Set '''
# # Creating Router Objects
# router = DefaultRouter()
#
# # Register StudentViewSet with Router
# router.register('message', ViewSet.MessageViewSet, basename='message')
# urlpatterns = [
#     path('all/', include(router.urls)),
# ]

# urlpatterns = [
#     path('all/', ConcreateView.MessageList.as_view()),
#     path('post/', ConcreateView.CreateMessage.as_view()),
#     path('<int:pk>/', ConcreateView.RetrieveMessage.as_view()),
#     path('edit/<int:pk>/', ConcreateView.UpdateMessage.as_view()),
#     path('delete/<int:pk>/', ConcreateView.DestroyMessage.as_view())
# ]



# urlpatterns = [
#     path('set-session/', views.set_session, name='set-session'),
#     path('get-session/', views.get_session, name='get-session'),
# ]

# urlpatterns = [
#     path('all/', views.message_list),
#     path('<int:pk>/', views.message),
#     path('post/', views.MessagePost.as_view()),
#     path('edit/<int:pk>/', views.edit_message),
#     path('delete/<int:pk>/', views.delete_message)
# ]
