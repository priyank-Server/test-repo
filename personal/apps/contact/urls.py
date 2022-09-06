from django.contrib import admin
from django.urls import path
from apps.contact import views

urlpatterns = [
    path('', views.ContactView.as_view())
]

