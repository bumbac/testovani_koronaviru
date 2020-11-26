"""
View controller for reservations page
"""
from django.shortcuts import render
from django.views import View
from corona.forms import ReservationForm
from django.contrib import messages
from django.contrib.auth import login
from django.http import HttpResponseRedirect

from corona.data_layer.interfaces.data_access_factory import DataAccessFactory
from corona.business_layer.application_logic.interfaces.handler_factory import HandlerFactory


class ReservationView(View):
    form = ReservationForm
    data_access_factory = DataAccessFactory()
    handler_factory = HandlerFactory()

    def get(self, request):
        return render(request, 'corona/reservation.html', {'form': self.form})

    def post(self, request):
        form = self.form(request.POST)
        reservation_handler = self.handler_factory.get_reservation_handler()
        covidpass_data_access = self.data_access_factory.get_covidpass_data_access()
        patient_handler = self.handler_factory.get_patient_handler()
        if form.is_valid():
            print("Form valid")
            patient = patient_handler.get_patient(request.user)
            reservation_handler.create_reservation(form.cleaned_data['deadline'], patient, covidpass_data_access.get_covidpass(patient))
        else:
            messages.error(request, form.errors)
            print(form['deadline'])
        return render(request, 'corona/reservation.html', {'form': self.form})
