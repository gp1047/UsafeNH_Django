from django.contrib.auth.models import User
from django.db import models



class Thing(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    slug = models.SlugField(unique=True)
    user = models.ForeignKey(User, related_name='User', null=True)
