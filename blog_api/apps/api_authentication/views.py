from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from apps.core.serializers import UserSerializer
from apps.core.models import User


class UserListAPIView(ListCreateAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)

    queryset = User.objects.all()
    serializer_class = UserSerializer

    filterset_fields = ('username', 'first_name', 'last_name', 'email', 'is_active', 'last_login')
    search_fields = ('^username', '^first_name', '^last_name', '^email', '^is_active', '^last_login')
    ordering_fields = ('username', 'first_name', 'last_name', 'email', 'is_active', 'last_login')


class UserDetailAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)

    queryset = User.objects.all()
    serializer_class = UserSerializer