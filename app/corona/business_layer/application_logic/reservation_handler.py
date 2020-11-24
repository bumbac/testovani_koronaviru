from corona.business_layer.application_logic.interfaces.reservation_handler_interface import ReservationHandlerInterface
from corona.data_layer.reservation_data_access import ReservationDataAccess
from datetime import datetime


class ReservationHandler(ReservationHandlerInterface):
    def create_reservation(self, deadline, covidpass):
        reservation_data_access = ReservationDataAccess()
        reservation_data_access.add_reservation(datetime.now(), deadline, covidpass)
        return True
