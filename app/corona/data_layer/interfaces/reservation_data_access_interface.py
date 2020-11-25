from abc import ABC, abstractmethod


class ReservationDataAccessInterface(ABC):
    @abstractmethod
    def add_reservation(self, createdate, deadline, patient, covidpass):
        pass

    @abstractmethod
    def get_reservation(self, covidpass):
        pass
