from abc import ABC, abstractmethod


class PatientHandlerInterface(ABC):
    @abstractmethod
    def create_patient(self, name, surname, birthid, email, phone, address, user):
        pass

    @abstractmethod
    def get_patient(self, user):
        pass