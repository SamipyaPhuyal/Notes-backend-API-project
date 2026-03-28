from django.contrib import admin
from django.urls import include, path
from Dashboard.views import DashboardSerializerView
urlpatterns = [
    path('',DashboardSerializerView.as_view(),name="dashboard"),
]