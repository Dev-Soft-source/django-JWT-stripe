# accounts/urls.py

from django.urls import path
from .views import RegisterView, AdminOnlyView, CustomerOnlyView, ProtectedView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('admin-only/', AdminOnlyView.as_view(), name='admin-only'),
    path('customer-only/', CustomerOnlyView.as_view(), name='customer-only'),
    path('protected/', ProtectedView.as_view(), name='protected'),    
]
