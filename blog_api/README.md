from datetime import datetime
from django.utils import timezone
from django.utils.six import BytesIO
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from apps.blog.models import Tag, Post
from apps.blog.serializers import TagSerializer, PostSerializer
from django.contrib.auth.models import User
user = User.objects.get(pk=1)
p = Post(title="My title", body="My body", author=user)
p.save()
ps = PostSerializer(p)
print(ps)