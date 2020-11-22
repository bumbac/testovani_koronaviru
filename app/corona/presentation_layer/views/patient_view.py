from django.shortcuts import render
from django.views import View


class PatientView(View):
    def get(self, request):
        return render(request, 'corona/patient.html')
