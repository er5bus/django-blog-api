from django.urls import re_path

from . import views


urlpatterns = (
    re_path(r'^tags/$', views.TagListAPIView.as_view(), name='tag-list'),
    re_path(r'^tags/(?P<pk>\d+)/$', views.TagDetailAPIView.as_view(), name='tag-detail'),

    re_path(r'^posts/$', views.PostListAPIView.as_view(), name='post-list'),
    re_path('posts/<slug:slug>/', views.PostDetailAPIView.as_view(), name='post-detail'),

    re_path(r'^posts/(?P<slug>\w+)/tags/$', views.PostTagsListAPIView.as_view(), name='post-tag-list'),
    re_path(r'^posts/(?P<slug>\w+)/tags/(?P<pk>\d+)/$', views.PostTagsDetailAPIView.as_view(), name='post-tag-detail')
)