from django.shortcuts import render
from django.shortcuts  import render_to_response
from .models import TestUpload
from uSafeUS import settings
import sys,os
import csv
import django

# Create your views here.


def testUpload(request):
	csv_filepathname="C:/Users/rocky/Desktop/uSafeInDjango/uSafeUS/Static/files/testUpload.csv"
	your_djangoproject_home="C:/Users/rocky/Desktop/uSafeInDjango/uSafeUS/"
	sys.path.append(your_djangoproject_home)
	os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myapp.settings")
	django.setup()
	dataReader = csv.reader(open(csv_filepathname), delimiter=',', quotechar='"')
	for row in dataReader:
		if row[0] != 'collegeName': 
			upload = TestUpload()
			upload.collegeName = row[0]
			upload.collegeCity = row[1]
			upload.save()
	return render(request,'testUpload.html',{})