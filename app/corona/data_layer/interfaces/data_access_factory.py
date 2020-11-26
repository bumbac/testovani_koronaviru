from corona.data_layer.covidpass_data_access import CovidpassDataAccess
from corona.data_layer.reservation_data_access import ReservationDataAccess
from corona.data_layer.covidtest_data_access import CovidtestDataAccess
from corona.data_layer.patient_data_access import PatientDataAccess
from corona.data_layer.user_data_access import UserDataAccess


class DataAccessFactory:
    def _get_covidpass_data_access(self):
        return CovidpassDataAccess()

    def _get_covidtest_data_access(self):
        return CovidtestDataAccess()

    def _get_reservation_data_access(self):
        return ReservationDataAccess()

    def _get_patient_data_access(self):
        return PatientDataAccess()

    def _get_user_data_access(self):
        return UserDataAccess()
