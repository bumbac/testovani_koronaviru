from corona.data_layer.interfaces.covidpass_data_access_interface import CovidpassDataAccessInterface
from corona.models import CovidPass


class CovidpassDataAccess(CovidpassDataAccessInterface):
    def add_covidpass(self, patient, covidtest):
        covidpass = CovidPass(patient=patient, covidtest=covidtest)
        covidpass.save()
        return True

    def get_covidpass(self, patient):
        print(f'patient: {patient}')
        return CovidPass.objects.filter(patient=patient)[0]