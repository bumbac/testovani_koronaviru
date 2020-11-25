"""
View controller for doctor's index page
"""
from django.shortcuts import render
from django.views import View


class DoctorView(View):
    def get(self, request):
        return render(request, 'corona/doctor.html')