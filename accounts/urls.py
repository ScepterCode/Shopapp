from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'users', views.CustomUserViewSet)
router.register(r'activities', views.UserActivityViewSet, basename='activity')

urlpatterns = [
    path('', include(router.urls)),
]