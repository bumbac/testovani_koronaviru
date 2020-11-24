from abc import ABC, abstractmethod


class PatientDataAccessInterface(ABC):
    @abstractmethod
    def add_patient(self, name, surname, birthid, email, phone, address, user):
        pass

    def get_patient(self):
        pass