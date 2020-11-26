from corona.business_layer.application_logic.patient_handler import PatientHandler
from corona.business_layer.application_logic.covidpass_handler import CovidpassHandler
from corona.business_layer.application_logic.reservation_handler import ReservationHandler
from corona.business_layer.application_logic.user_handler import UserHandler


class HandlerFactory:
    def _get_patient_handler(self):
        return PatientHandler()

    def _get_covidpass_handler(self):
        return CovidpassHandler()

    def _get_reservation_handler(self):
        return ReservationHandler()

    def _get_user_handler(self):
        return UserHandler()