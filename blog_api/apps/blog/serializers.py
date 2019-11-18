from rest_framework import serializers

from .models import Post, Tag

from apps.core.serializers import UserSerializer


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'


class PostSerializer(serializers.ModelSerializer):
    created = serializers.DateTimeField(read_only=True, format="%d/%m/%Y %H:%M:%S")
    updated = serializers.DateTimeField(read_only=True, format="%d/%m/%Y %H:%M:%S")

    tags = TagSerializer(many=True)
    author = UserSerializer(read_only=True)

    class Meta:
        model = Post
        exclude = ('slug', )

