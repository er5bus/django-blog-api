from rest_framework import serializers

from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password', 'first_name', 'last_name', 'email', 'is_active', 'last_login')
        extra_kwargs = {'password': {'write_only': True}, 'last_login': {'format': '%D %H:%M:%S', 'read_only': True},
                        'is_active': {'read_only': True}}
