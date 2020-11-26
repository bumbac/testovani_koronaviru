from corona.business_layer.application_logic.patient_handler import PatientHandler
from corona.business_layer.application_logic.covidpass_handler import CovidpassHandler
from corona.business_layer.application_logic.reservation_handler import ReservationHandler
from corona.business_layer.application_logic.user_handler import UserHandler


class HandlerFactory:
    patient_handler = PatientHandler()
    covidpass_handler = CovidpassHandler()
    reservation_handler = ReservationHandler()
    user_handler = UserHandler()

    def _get_patient_handler(self):
        return self.patient_handler

    def _get_covidpass_handler(self):
        return self.covidpass_handler

    def _get_reservation_handler(self):
        return self.reservation_handler

    def _get_user_handler(self):
        return self.user_handler
