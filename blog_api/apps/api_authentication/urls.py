from django.urls import path

from rest_framework_simplejwt import views as simplejwt_views
from . import views as user_views


urlpatterns = (
    path('token/refresh/', simplejwt_views.TokenRefreshView.as_view(), name='token-refresh'),
    path('token/verify/', simplejwt_views.TokenVerifyView.as_view(), name='token-verify'),
    path('token/', simplejwt_views.TokenObtainPairView.as_view(), name='token-obtain-pair'),

    path('users/', user_views.UserListAPIView.as_view(), name='user-list'),
    path('users/<int:pk>/', user_views.UserDetailAPIView.as_view(), name='user-detail')
)