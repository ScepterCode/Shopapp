from django.shortcuts import render

from rest_framework import viewsets, status, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from .models import CustomUser, UserActivity
from .serializers import CustomUserSerializer, UserActivitySerializer

class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_permissions(self):
        if self.action == 'create':
            return [permissions.AllowAny()]
        return super().get_permissions()

    @action(detail=False, methods=['post'])
    def login(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        
        user = authenticate(username=username, password=password)
        if user:
            refresh = RefreshToken.for_user(user)
            UserActivity.objects.create(
                user=user,
                activity_type='login',
                description='User logged in',
                ip_address=request.META.get('REMOTE_ADDR')
            )
            return Response({
                'token': str(refresh.access_token),
                'refresh': str(refresh),
                'user': CustomUserSerializer(user).data
            })
        return Response(
            {'error': 'Invalid credentials'}, 
            status=status.HTTP_401_UNAUTHORIZED
        )

    @action(detail=False, methods=['post'])
    def change_password(self, request):
        user = request.user
        old_password = request.data.get('old_password')
        new_password = request.data.get('new_password')
        
        if not user.check_password(old_password):
            return Response(
                {'error': 'Invalid old password'}, 
                status=status.HTTP_400_BAD_REQUEST
            )
            
        user.set_password(new_password)
        user.save()
        UserActivity.objects.create(
            user=user,
            activity_type='password_change',
            description='User changed password',
            ip_address=request.META.get('REMOTE_ADDR')
        )
        return Response({'message': 'Password updated successfully'})

class UserActivityViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = UserActivitySerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        if self.request.user.user_type == 'admin':
            return UserActivity.objects.all()
        return UserActivity.objects.filter(user=self.request.user)

