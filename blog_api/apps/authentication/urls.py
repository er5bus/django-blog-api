from django.urls import re_path

from rest_framework.urls import views as django_auth_views


urlpatterns = (
    # Login logout urls
    re_path(r'^login/$', django_auth_views.LoginView.as_view(
        template_name='authentication/login.html'
    ), name='login'),
    re_path(r'^logout/$', django_auth_views.LogoutView.as_view(
        template_name='authentication/logged_out.html'
    ), name='logout')
)