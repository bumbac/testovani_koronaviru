from abc import ABC, abstractmethod


class PatientDataAccessInterface(ABC):
    @abstractmethod
    def add_patient(self, name, surname, birthid, email, phone, address, user):
        pass

    @abstractmethod
    def get_patient(self, user_id):
        pass
