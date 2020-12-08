from abc import ABC, abstractmethod

"""
Interface of CovidpassHandler
"""
class CovidpassHandlerInterface(ABC):
    @abstractmethod
    def create_covidpass(self, patient, covidtest):
        """
        :param patient: patient_id
        :param covidtest: covidtest_id
        :return: True if successful, otherwise False
        """
        pass
