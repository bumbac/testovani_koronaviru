from abc import ABC, abstractmethod


class CovidpassHandlerInterface(ABC):
    @abstractmethod
    def create_covidpass(self, patient, covidtest):
        pass
