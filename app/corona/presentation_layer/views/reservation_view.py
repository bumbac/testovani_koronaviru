from django.shortcuts import render
from django.views import View
from corona.forms import ReservationForm
from django.contrib import messages
from django.contrib.auth import login
from django.http import HttpResponseRedirect

from corona.data_layer.user_data_access import UserDataAccess
from corona.business_layer.application_logic.user_handler import UserHandler


class ReservationView(View):
    form = ReservationForm

    def get(self, request):
        return render(request, 'corona/reservation.html', {'form': self.form})

    def post(self, request):
        return render(request, 'corona/reservation.html', {'form': self.form})