from django.forms import ModelForm

from webPortal.models import College
from webPortal.models import Hospital

class CollegeForm(ModelForm):
    class Meta:
        model = College
        fields = ('collegeName', 'collegeAddress', 'collegeTown','hospital',)

class HospitalForm(ModelForm):
    class Meta:
        model = Hospital
        fields = ('hospitalName', 'hospitalAddress', 'hospitalPhoneNumber', 'hospitalDirections',)
