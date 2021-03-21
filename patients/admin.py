from django.contrib import admin
from .models import Patient, Record

admin.site.register(Patient)
admin.site.register(Record)
