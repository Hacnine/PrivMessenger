from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenVerifyView, TokenRefreshView

urlpatterns = [
    path('gettotken/', TokenObtainPairView.as_view(), name='gettotken'),
    path('refreshtoken', TokenRefreshView.as_view(), name='refreshtoken'),
    path('tokenverify/', TokenVerifyView.as_view(), name='tokenverify'),
]
