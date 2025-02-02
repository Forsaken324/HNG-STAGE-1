from django.urls import path
from . import views

urlpatterns = [
    path('classify-number/', views.classify_number)
]