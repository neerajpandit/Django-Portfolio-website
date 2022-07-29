from django.contrib import admin
from django.urls import path,include
from resumeapp import views
urlpatterns = [
    path('',views.index, name="home"),
]