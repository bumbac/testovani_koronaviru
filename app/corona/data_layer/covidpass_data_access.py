from corona.data_layer.interfaces.covidpass_data_access_interface import CovidpassDataAccessInterface
from corona.models import CovidPass


class CovidpassDataAccess(CovidpassDataAccessInterface):
    def add_covidpass(self, patient, covidtest):
        covidpass = CovidPass(patient, covidtest)
        covidpass.save()
        return True
