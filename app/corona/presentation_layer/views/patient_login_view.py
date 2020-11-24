"""
View controller for patient's login page
"""
from django.shortcuts import render
from django.views import View
from corona.forms import LoginForm
from django.contrib import messages
from django.contrib.auth import login
from django.http import HttpResponseRedirect

from corona.data_layer.user_data_access import UserDataAccess
from corona.business_layer.application_logic.user_handler import UserHandler


class PatientLoginView(View):
    form = LoginForm

    def get(self, request):
        return render(request, 'corona/patient_login.html', {'form': self.form})

    def post(self, request):
        user_data_access = UserDataAccess()
        user_handler = UserHandler()
        form = self.form(request.POST)
        if form.is_valid():
            if user_handler.check_password(form.cleaned_data['username'], form.cleaned_data['password']):
                login(request, user_data_access.get_user(form.cleaned_data['username']))
                return HttpResponseRedirect(request.GET["next"] if "next" in request.GET else "/patient")
            else:
                messages.error(request, 'Spatne heslo')
        return render(request, 'corona/patient_login.html', {'form': form})