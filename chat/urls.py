from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('messages/', views.messages, name='messages'),
    path('send/', views.send_message, name='send_message'),
]
