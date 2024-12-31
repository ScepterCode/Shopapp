from django.urls import path
from . import views

urlpatterns = [
    path('', views.invoice_list, name='invoice_list'),
    path('<int:pk>/', views.invoice_detail, name='invoice_detail'),
    path('<int:pk>/items/', views.add_invoice_item, name='add_invoice_item'),
]
