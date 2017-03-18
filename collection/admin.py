from django.contrib import admin

# Register your models here.
# import your model
from collection.models import College
from collection.models import Hospital

# set up automated slug creation
class CollegeAdmin(admin.ModelAdmin):
    model = College
    list_display = ('collegeName', 'collegeAddress', 'collegeTown',)
    prepopulated_fields = {'slug': ('collegeName',)}

class HospitalAdmin(admin.ModelAdmin):
    model = Hospital
    list_display = ('hospitalName', 'hospitalAddress', 'hospitalPhoneNumber', 'hospitalDirections',)

# and register it
admin.site.register(College, CollegeAdmin)
admin.site.register(Hospital, HospitalAdmin)
