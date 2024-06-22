from django.contrib import admin
from django.urls import path
from django.urls import path,include
from resttest import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('users.urls')),
    path('course/', include('resttest.urls')),
    path('simplejwt/', include('simplejwt.urls'))

]
