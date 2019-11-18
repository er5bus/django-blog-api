from django.contrib.auth.models import User as BaseUser
from django.utils.translation import ugettext_lazy as _


class User(BaseUser):

    class Meta:
        proxy = True
        ordering = ['-id']

    def __str__(self):
        return self.username