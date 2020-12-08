"""
View controller for patient's login page
"""
from django.shortcuts import render
from django.views import View
from corona.forms import LoginForm
from django.contrib import messages
from django.contrib.auth import login
from django.http import HttpResponseRedirect

from corona.data_layer.interfaces.data_access_factory import DataAccessFactory
from corona.business_layer.handlers.interfaces.handler_factory import HandlerFactory


class PatientLoginView(View):
    form = LoginForm
    data_access_factory = DataAccessFactory()
    handler_factory = HandlerFactory()

    def get(self, request):
        return render(request, 'corona/patient_login.html', {'form': self.form})

    def post(self, request):
        user_data_access = self.data_access_factory.get_user_data_access()
        user_handler = self.handler_factory.get_user_handler()
        form = self.form(request.POST)
        if form.is_valid():
            if user_handler.check_password(form.cleaned_data['username'], form.cleaned_data['password']):
                login(request, user_data_access.get_user(form.cleaned_data['username']))
                return HttpResponseRedirect(request.GET["next"] if "next" in request.GET else "/patient")
            else:
                messages.error(request, 'Spatne heslo')
        return render(request, 'corona/patient_login.html', {'form': form})
