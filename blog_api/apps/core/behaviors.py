from django.db import models
from django.conf import settings


class Timestampable(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Authorable(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def is_owner(self, author):
        return self.author == author

    class Meta:
        abstract = True
