from django.urls import path

from .views import *

urlpatterns = [
    path('/<str:testid>/', test)
]