from abc import ABC, abstractmethod


class ReservationHandlerInterface(ABC):
    @abstractmethod
    def create_reservation(self, deadline, covidpass):
        pass
