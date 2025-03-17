from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('',views.index,name="product_index"),
    path('create/',views.createView,name="product_create_view"),
    path('view/',views.viewer,name="product_view"),
]