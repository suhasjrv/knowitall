from django.contrib import admin
from main_app import views
from django.conf.urls import url

urlpatterns = [
    url('r^/index', views.index, name = "index"),
]
