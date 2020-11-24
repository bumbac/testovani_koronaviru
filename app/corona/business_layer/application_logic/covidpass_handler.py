from corona.business_layer.application_logic.interfaces.covidpass_handler_interface import CovidpassHandlerInterface
from corona.data_layer.covidpass_data_access import CovidpassDataAccess


class CovidpassHandler(CovidpassHandlerInterface):
    def create_covidpass(self, patient, covidtest):
        covidpass_data_access = CovidpassDataAccess()
        covidpass_data_access.add_covidpass(patient=patient, covidtest=covidtest)
        return True
