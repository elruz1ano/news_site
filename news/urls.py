from django.urls import path

from . import views

urlpatterns = [
    path('', views.in_news, name='in_news'),
]