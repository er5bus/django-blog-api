from django.db import models

from apps.core.fields import AutoSlugField
from apps.core.behaviors import Authorable, Timestampable


class Tag(models.Model):
    name = models.CharField(max_length=150, unique=True)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.name


class Post(Authorable, Timestampable):
    title = models.CharField(max_length=150)
    slug = AutoSlugField(populate_from='title', max_length=250)
    body = models.TextField(max_length=10000)

    tags = models.ManyToManyField(Tag, related_name='post')

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.title