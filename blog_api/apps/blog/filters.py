from django_filters import filterset

from .models import Post


class PostFilter(filterset.FilterSet):
    class Meta:
        model = Post
        fields = ('title', 'body', 'created', 'updated')