from corona.data_layer.covidpass_data_access import CovidpassDataAccess
from corona.data_layer.reservation_data_access import ReservationDataAccess
from corona.data_layer.covidtest_data_access import CovidtestDataAccess
from corona.data_layer.patient_data_access import PatientDataAccess
from corona.data_layer.user_data_access import UserDataAccess


class DataAccessFactory:
    covidpass_data_access = CovidpassDataAccess()
    covidtest_data_access = CovidtestDataAccess()
    reservation_data_access = ReservationDataAccess()
    patient_data_access = PatientDataAccess()
    user_data_access = UserDataAccess()

    def _get_covidpass_data_access(self):
        return self.covidpass_data_access

    def _get_covidtest_data_access(self):
        return self.covidtest_data_access

    def _get_reservation_data_access(self):
        return self.reservation_data_access

    def _get_patient_data_access(self):
        return self.patient_data_access

    def _get_user_data_access(self):
        return self.user_data_access
