from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .serializers import TagSerializer, PostSerializer
from .models import Tag, Post
from .filters import PostFilter

from apps.core.permissions import IsCurrentUserOwnerOrReadOnly


class TagListAPIView(ListCreateAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)

    queryset = Tag.objects.all()
    filterset_fields = ('name',)
    search_fields = ('^name',)
    ordering_fields = ('name',)

    serializer_class = TagSerializer


class TagDetailAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)

    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class PostListAPIView(ListCreateAPIView):
    permission_classes = (IsCurrentUserOwnerOrReadOnly,)

    queryset = Post.objects.all()
    serializer_class = PostSerializer
    filterset_class = PostFilter

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class PostDetailAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsCurrentUserOwnerOrReadOnly,)

    queryset = Post.objects.all()
    serializer_class = PostSerializer

    lookup_field = 'slug'


class PostTagsListAPIView(ListCreateAPIView):
    serializer_class = TagSerializer

    def get_queryset(self):
        return Tag.objects.filter(post__slug=self.kwargs.get('slug'))

    def perform_create(self, serializer):
        tag = serializer.save()
        post = Post.objects.filter(slug=self.kwargs.get('slug')).get()
        post.tags.add(tag)
        post.save()


class PostTagsDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = TagSerializer

    def get_queryset(self):
        return Tag.objects.filter(post__slug=self.kwargs.get('slug'))