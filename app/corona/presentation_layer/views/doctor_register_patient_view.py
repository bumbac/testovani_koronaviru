"""
View controller for doctor's pacient registration page
"""
from django.shortcuts import render
from django.views import View
from django.http import HttpResponseRedirect
from django.contrib.auth import login

from corona.business_layer.application_logic.user_handler import UserHandler
from corona.business_layer.application_logic.patient_handler import PatientHandler
from corona.business_layer.application_logic.covidpass_handler import CovidpassHandler
from corona.data_layer.user_data_access import UserDataAccess
from corona.data_layer.covidtest_data_access import CovidtestDataAccess
from corona.forms import PatientRegisterForm


class DoctorRegisterPatientView(View):
    form = PatientRegisterForm

    def get(self, request):
        return render(request, 'corona/doctor_register_patient.html', dict(form=self.form))

    def post(self, request):
        user_handler = UserHandler()
        patient_handler = PatientHandler()
        user_data_access = UserDataAccess()
        covid_pass_handler = CovidpassHandler()
        covidtest_data_access = CovidtestDataAccess()
        form = self.form(request.POST)
        if form.is_valid():
            user_handler.create_user(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            user = user_data_access.get_user(form.cleaned_data['username'])
            patient_handler.create_patient(name=form.cleaned_data['name'], surname=form.cleaned_data['surname'], birthid=form.cleaned_data['birthid'], email=form.cleaned_data['email'], phone=form.cleaned_data['phone'], address=form.cleaned_data['address'], user=user)
            covid_pass_handler.create_covidpass(patient_handler.get_patient(user), covidtest_data_access.get_covidtest(form.cleaned_data['covidtest']))
            return HttpResponseRedirect('/doctor')
        else:
            print("Invalid form")
            return render(request, 'corona/doctor_register_patient.html', dict(form=self.form))
