from django.forms import ModelForm
from django.forms import modelformset_factory
from webPortal.models import College
from webPortal.models import Hospital

class CollegeForm(ModelForm):
    class Meta:
        model = College
        fields = ('collegeName', 'collegeAddress', 'collegeTown',)

class HospitalForm(ModelForm):
    class Meta:
        model = Hospital
        fields = ('hospitalName', 'hospitalAddress', 'hospitalPhoneNumber', 'hospitalDirections',)

HospitalFormSet = modelformset_factory(Hospital, form=HospitalForm)
