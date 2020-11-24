from django.shortcuts import render
from django.views import View
from corona.forms import ReservationForm
from django.contrib import messages
from django.contrib.auth import login
from django.http import HttpResponseRedirect

from corona.business_layer.application_logic.reservation_handler import ReservationHandler
from corona.data_layer.covidpass_data_access import CovidpassDataAccess
from corona.business_layer.application_logic.patient_handler import PatientHandler


class ReservationView(View):
    form = ReservationForm

    def get(self, request):
        return render(request, 'corona/reservation.html', {'form': self.form})

    def post(self, request):
        form = self.form(request.POST)
        reservation_handler = ReservationHandler()
        covidpass_data_access = CovidpassDataAccess()
        patient_handler = PatientHandler()
        if form.is_valid():
            print("Form valid")
            patient = patient_handler.get_patient(request.user)
            reservation_handler.create_reservation(form.cleaned_data['deadline'], patient, covidpass_data_access.get_covidpass(patient))
        else:
            messages.error(request, form.errors)
            print(form['deadline'])
        return render(request, 'corona/reservation.html', {'form': self.form})
