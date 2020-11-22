from django.shortcuts import render
from django.views import View
from django.http import HttpResponse

from corona.business_layer.application_logic.user_handler import UserHandler
from corona.business_layer.application_logic.patient_handler import PatientHandler
from corona.data_layer.user_data_access import UserDataAccess
from corona.forms import PatientRegisterForm


class RegisterPatientView(View):
    form = PatientRegisterForm

    def get(self, request):
        return render(request, 'corona/register_patient.html', dict(form=self.form))

    def post(self, request):
        user_handler = UserHandler()
        patient_handler = PatientHandler()
        user_data_acces = UserDataAccess()
        form = self.form(request.POST)
        if form.is_valid():
            print("Form is valid")
            user_handler.create_user(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            print("Saved user")
            patient_handler.create_patient(name=form.cleaned_data['name'], surname=form.cleaned_data['surname'], birthid=form.cleaned_data['birthid'], email=form.cleaned_data['email'], phone=form.cleaned_data['phone'], address=form.cleaned_data['address'], user=user_data_acces.get_user(form.cleaned_data['username'])[0])
            print("Saved patient")
            return HttpResponse('Great success, very nice!')
        else:
            print("Invalid form")
            return render(request, 'corona/register_patient.html', dict(form=self.form))
