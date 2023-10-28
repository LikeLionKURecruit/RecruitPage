from django.urls import path, include
from django.contrib import admin
from . import views

urlpatterns = [
    path("",views.main),
    path("/<int:year>/<int:team>/",views.detail,name='detail'),
]
