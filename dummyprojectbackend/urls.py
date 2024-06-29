from django.contrib import admin
from django.urls import path
from django.urls import path,include
urlpatterns = [
    path('admin/', admin.site.urls),
    path('msg/', include('users.urls')),
    path('auth/', include('rest_framework.urls'))
]
