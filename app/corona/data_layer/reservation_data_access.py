from corona.data_layer.interfaces.reservation_data_access_interface import ReservationDataAccessInterface
from corona.models import Reservation


class ReservationDataAccess(ReservationDataAccessInterface):
    def add_reservation(self, createdate, deadline, patient, covidpass):
        reservation = Reservation(createdate=createdate, deadline=deadline, patient=patient, covidpass=covidpass)
        reservation.save()
        return True

    def get_reservation(self, covidpass):
        pass
