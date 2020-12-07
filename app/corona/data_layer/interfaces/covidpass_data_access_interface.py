from abc import ABC, abstractmethod


class CovidpassDataAccessInterface(ABC):
    @abstractmethod
    def add_covidpass(self, patient, covidtest):
        pass

    @abstractmethod
    def get_active_covidpass(self, patient):
        pass

    @abstractmethod
    def get_all_patients_covidpasses(self, patient):
        pass