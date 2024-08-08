from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/user/', include('account.urls')),  # For user-related endpoints
    path('api/messages/', include('users.urls')),    # For message-related endpoints
    path('auth/', include('rest_framework.urls')),  # For DRF authentication
]
