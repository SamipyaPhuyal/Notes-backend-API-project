from django.contrib import admin
from django.urls import path
from Users.views import RegistrationView, UserViewSet
urlpatterns = [
    path('list/', UserViewSet.as_view(), name='users-list-create'),
    path('detail/<int:pk>/', UserViewSet.as_view(), name='users-detail'),
    path('register/', RegistrationView.as_view(), name='users-register'),
]
