from django.contrib.auth.models import User
from corona.data_layer.interfaces.patient_data_access_interface import PatientDataAccessInterface
from corona.models import Patient


class PatientDataAccess(PatientDataAccessInterface):
    def add_patient(self, name, surname, birthid, email, phone, address, user):
        patient = Patient(name=name, surname=surname, birthid=birthid, email=email, phone=phone, address=address, user=user)
        patient.save()
        return True
