from django.urls import path
from . import views

# URL patterns for quotation endpoints
urlpatterns = [
    path('', views.quotation_list, name='quotation_list'),  # List and create quotations
    path('<int:pk>/', views.quotation_detail, name='quotation_detail'),  # Retrieve, update, or delete a specific quotation
    path('<int:pk>/items/', views.add_quotation_item, name='add_quotation_item'),  # Add items to a specific quotation
]
