from abc import ABC, abstractmethod

"""
Interface of ReservationHandler
"""
class ReservationHandlerInterface(ABC):
    @abstractmethod
    def create_reservation(self, deadline, patient, covidpass):
        """
        :param deadline: Deadline
        :param patient: Patient
        :param covidpass: Covidpass
        :return: True if successful, otherwise False
        """
        pass
