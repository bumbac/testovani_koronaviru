from django.shortcuts import render
from django.views import View
from corona.forms import ReservationForm
from django.contrib import messages
from django.contrib.auth import login
from django.http import HttpResponseRedirect

from corona.data_layer.reservation_data_access import ReservationDataAccess
from corona.business_layer.application_logic.user_handler import UserHandler


class ReservationView(View):
    form = ReservationForm

    def get(self, request):
        return render(request, 'corona/reservation.html', {'form': self.form})

    def post(self, request):
        form = self.form(request.POST)
        reservation_data_access = ReservationDataAccess()
        if form.is_valid():
            print("Form valid")
            reservation_data_access.add_reservation()
        else:
            messages.error(request, form.errors)
            print(form['deadline'])
        return render(request, 'corona/reservation.html', {'form': self.form})
