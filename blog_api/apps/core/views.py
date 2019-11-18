from rest_framework.generics import GenericAPIView
from rest_framework.reverse import reverse
from rest_framework.response import Response


class APIRoot(GenericAPIView):

    def get(self, request, *args, **kwargs):
        return Response({
            "tags": reverse(viewname='tag-list', request=request),
            "posts": reverse(viewname='post-list', request=request),
            "users": reverse(viewname='user-list', request=request),
            "token_refresh": reverse(viewname='token-refresh', request=request),
            "token_verify": reverse(viewname='token-verify', request=request),
            "token_obtain_pair": reverse(viewname='token-obtain-pair', request=request)
        })