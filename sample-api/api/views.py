from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import viewsets, generics
from django.contrib.auth.models import User
from api import models, serializers


class UserViewSet(viewsets.ModelViewSet):
    """Handles CRUD"""
    permission_classes = (AllowAny,)
    serializer_class = serializers.UserSerializer
    queryset = User.objects.all()


class ManageUserView(generics.RetrieveUpdateAPIView):
    """Manage the authenticated user"""
    serializer_class = serializers.UserSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get_object(self):
        return self.request.user                        # current authenticated user


class TaskViewSet(viewsets.ModelViewSet):
    """Handles CRUD"""
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    serializer_class = serializers.TaskSerializer
    queryset = models.Task.objects.all()
