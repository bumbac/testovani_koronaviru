from corona.data_layer.interfaces.reservation_data_access_interface import ReservationDataAccessInterface
from corona.data_layer.models import Reservation


class ReservationDataAccess(ReservationDataAccessInterface):
    def add_reservation(self, createdate, deadline, covidpass):
        reservation = Reservation(createdate=createdate, deadline=deadline, covidpass=covidpass)
        reservation.save()
        return True

    def get_reservation(self, covidpass):
        pass
