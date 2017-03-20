from django.contrib.auth.models import User
from django.db import models


class Hospital(models.Model):
    hospitalName = models.CharField(max_length=100)
    hospitalAddress = models.CharField(max_length=100)
    hospitalPhoneNumber = models.CharField(max_length=100)
    hospitalDirections = models.CharField(max_length=255)
    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return self.hospitalName

class College(models.Model):
    collegeName = models.CharField(max_length=100)
    collegeAddress = models.CharField(max_length=100)
    collegeTown = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    user = models.ForeignKey(User, related_name='College', null=True)
    hospital = models.ManyToManyField(Hospital, related_name='Hospital', null=True)
    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return self.collegeName
