from django.contrib.auth.models import User
from django.db import models



class College(models.Model):
    collegeName = models.CharField(max_length=255)
    collegeAddress = models.CharField(max_length=255)
    collegeTown = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    user = models.ForeignKey(User, related_name='College', null=True)

class Hospital(models.Model):
    hospitalName = models.CharField(max_length=255)
    hospitalAddress = models.CharField(max_length=255)
    hospitalPhoneNumber = models.CharField(max_length=255)
    hospitalDirections = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    user = models.ForeignKey(User, related_name='Hospital', null=True)
    college = models.ForeignKey(College.collegeName, related_name='Hospital', null=True)
