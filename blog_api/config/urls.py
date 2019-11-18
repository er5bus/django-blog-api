"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path, re_path, include
from django.conf import settings


urlpatterns = [
    # Django rest framework
    #re_path(r'^api-auth/', include('rest_framework.urls')),

    # Admin URLs (No need to the admin)
    #re_path(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    #re_path(r'^admin/', admin.site.urls),

    re_path(r'^auth/', include('apps.authentication.urls')),

    # REST API
    re_path(r'^api/v1/auth/', include('apps.api_authentication.urls')),
    re_path(r'^api/v1/blog/', include('apps.blog.urls')),

    # REST API ROOT
    re_path(r'^', include('apps.core.urls'))
]

if settings.DEBUG:

    try:
        from django.conf.urls.static import static
        import debug_toolbar
        urlpatterns += [
            re_path(r'^__debug__/', include(debug_toolbar.urls))
        ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

    # Should only occur when debug mode is on for production testing
    except ImportError as e:
        import logging
        l = logging.getLogger(__name__)
        l.warning(e)
