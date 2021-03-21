from django.shortcuts import render, get_object_or_404
from django.http import Http404

from .models import Patient, Record

def index(request):
    patient_list = Patient.objects.all()
    return render(request, 'patients/index.html', {'patient_list': patient_list})

def detail(request, patient_id):
    patient = get_object_or_404(Patient, pk=patient_id)
    return render(request, 'patients/detail.html', {'patient': patient})
