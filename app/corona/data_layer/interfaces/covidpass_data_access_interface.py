from abc import ABC, abstractmethod


class CovidpassDataAccessInterface(ABC):
    @abstractmethod
    def add_covidpass(self, patient, covidtest):
        pass
