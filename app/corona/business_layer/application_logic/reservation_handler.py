from corona.business_layer.application_logic.interfaces.reservation_handler_interface import ReservationHandlerInterface
from corona.data_layer.reservation_data_access import ReservationDataAccess
from datetime import datetime


"""
Implementation of ReservationHandler interface
"""
class ReservationHandler(ReservationHandlerInterface):
    def create_reservation(self, deadline, patient, covidpass):
        reservation_data_access = ReservationDataAccess()
        reservation_data_access.add_reservation(createdate=datetime.now().strftime('%Y-%m-%d %H:%M'), deadline=deadline, patient=patient, covidpass=covidpass)
        return True
