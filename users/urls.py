from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from . import views, GenericApiView, ConcreateView, ViewSet, ModelViewSet
from rest_framework.routers import DefaultRouter
from .auth import CustomAuthToken

''' For ModelView Set '''
# Creating Router Objects
router = DefaultRouter()

# Register StudentViewSet with Router
router.register('message', ModelViewSet.MessageModelViewSet, basename='message')
# router.register('read_only_message', ModelViewSet.MessageReadOnlyModelViewSet, basename='model_view_set_message')

urlpatterns = [
    path('all/', include(router.urls)),
    # path('allreadonly/', include(router.urls)),
    # path('gettoken/', CustomAuthToken.as_view())
]

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
#     path('all/', GenericApiView.MessageList.as_view()),
#     path('post/', GenericApiView.CreateMessage.as_view()),
#     path('<int:pk>/', GenericApiView.RetrieveMessage.as_view()),
#     path('edit/<int:pk>/', GenericApiView.UpdateMessage.as_view()),
#     path('delete/<int:pk>/', GenericApiView.DestroyMessage.as_view())
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