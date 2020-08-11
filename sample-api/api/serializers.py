from rest_framework import serializers

from api.models import Task
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token


class UserSerializer(serializers.ModelSerializer):
    """Serializer for User objects"""

    class Meta:
        model = User
        fields = ('id', 'username', 'password')
        extra_kwargs = {'password': {'write_only': True, 'required': True}}
    
    def create(self, validated_data):
        """Create a new user with encrypted password and return it"""
        user = User.objects.create_user(**validated_data)
        Token.objects.create(user=user)
        return user


class TaskSerializer(serializers.ModelSerializer):
    """Serializer for Task objects"""

    class Meta:
        model = Task
        fields = ('id', 'title', 'created_at', 'updated_at')
        read_only_fields = ('created_at', 'updated_at')