from django.contrib import admin
from django.urls import path
from Users.views import RegistrationView, UserViewSet
from Users.views import LogoutView, RegistrationView, UserViewSet
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('list/', UserViewSet.as_view(), name='users-list-create'),
    path('detail/<int:pk>/', UserViewSet.as_view(), name='users-detail'),
    path('register/', RegistrationView.as_view(), name='users-register'),
    path('login/', TokenObtainPairView.as_view(), name='users-login'),
    path('refresh-token/', TokenRefreshView.as_view(), name='token_refresh'),
    path('logout/', LogoutView.as_view(), name='users-logout'),
]
