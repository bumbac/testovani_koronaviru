from corona.data_layer.covidpass_data_access import CovidpassDataAccess
from corona.data_layer.reservation_data_access import ReservationDataAccess
from corona.data_layer.covidtest_data_access import CovidtestDataAccess
from corona.data_layer.patient_data_access import PatientDataAccess
from corona.data_layer.user_data_access import UserDataAccess


class DataAccessFactory:
    __covidpass_data_access = CovidpassDataAccess()
    __covidtest_data_access = CovidtestDataAccess()
    __reservation_data_access = ReservationDataAccess()
    __patient_data_access = PatientDataAccess()
    __user_data_access = UserDataAccess()

    def get_covidpass_data_access(self):
        return self.__covidpass_data_access

    def get_covidtest_data_access(self):
        return self.__covidtest_data_access

    def get_reservation_data_access(self):
        return self.__reservation_data_access

    def get_patient_data_access(self):
        return self.__patient_data_access

    def get_user_data_access(self):
        return self.__user_data_access
