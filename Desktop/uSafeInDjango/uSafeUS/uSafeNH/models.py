from django.db import models

# Create your models here.
class TestUpload(models.Model):
	collegeName = models.CharField(max_length=250)
	collegeCity = models.CharField(max_length=250)
	
	def __unicode__(self):
 		return "%s, %s" % (self.collegeName, self.collegeCity)

	class Meta:
 		ordering = ['collegeName']