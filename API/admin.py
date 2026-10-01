from django.contrib import admin
from .models import Doctor, Patient

# Register your models here.
class DoctorAdmin(admin.ModelAdmin):
    list_display = ('name', 'specialization', 'qualification', 'experience', 'department', 'timing')
    search_fields = ('name', 'specialization', 'department')
admin.site.register(Doctor, DoctorAdmin)

class PatientAdmin(admin.ModelAdmin):
   list_display = ('patient_name', 'father_name', 'age', 'gender', 'mobile', 'address', 'problem', 'created_at')
   search_fields = ('patient_name', 'father_name', 'mobile')
admin.site.register(Patient, PatientAdmin)

