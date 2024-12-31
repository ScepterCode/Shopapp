from django.urls import path
from . import views

urlpatterns = [
    path('', views.receipt_list, name='receipt_list'),
    path('<int:pk>/', views.receipt_detail, name='receipt_detail'),
]
