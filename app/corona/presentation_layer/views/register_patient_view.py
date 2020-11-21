from django.shortcuts import render
from django.views import View

from corona.forms import PatientRegisterForm

class RegisterPatientView(View):
    def get(self, request):
        return render(request, 'corona/register_patient.html', dict(form=PatientRegisterForm()))
