from django.forms import ModelForm

from collection.models import College
from collection.models import Hospital

class CollegeForm(ModelForm):
    class Meta:
        model = College
        fields = ('collegeName', 'collegeAddress', 'collegeTown',)

class HospitalForm(ModelForm):
    class Meta:
        model = Hospital
        fields = ('hospitalName', 'hospitalAddress', 'hospitalPhoneNumber', 'hospitalDirections',)
