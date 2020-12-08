from corona.business_layer.handlers.patient_handler import PatientHandler
from corona.business_layer.handlers.covidpass_handler import CovidpassHandler
from corona.business_layer.handlers.reservation_handler import ReservationHandler
from corona.business_layer.handlers.user_handler import UserHandler


class HandlerFactory:
    __patient_handler = PatientHandler()
    __covidpass_handler = CovidpassHandler()
    __reservation_handler = ReservationHandler()
    __user_handler = UserHandler()

    def get_patient_handler(self):
        return self.__patient_handler

    def get_covidpass_handler(self):
        return self.__covidpass_handler

    def get_reservation_handler(self):
        return self.__reservation_handler

    def get_user_handler(self):
        return self.__user_handler
