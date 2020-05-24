from django.urls import path
from buyer import views

urlpatterns = [
    path('index/', views.index),
    path('goods_detail/', views.goods_detail),
    path('register/', views.register),
    path('login/', views.login),
]
