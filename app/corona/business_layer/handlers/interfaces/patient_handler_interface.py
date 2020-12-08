from abc import ABC, abstractmethod

"""
Interface of PatientHandler
"""
class PatientHandlerInterface(ABC):
    @abstractmethod
    def create_patient(self, name, surname, birthid, email, phone, address, user):
        """
        :param name: Name of the patient
        :param surname: Surname of the patient
        :param birthid: BirthID of the patient
        :param email: Email address of the patient
        :param phone: Phone number of the patient
        :param address: Address of the patient
        :param user: user_id of User, of whom this Patient belongs to
        :return: True if successful, otherwise False
        """
        pass

    @abstractmethod
    def get_patient(self, user):
        """
        :param user: user_id
        :return: Patient
        """
        pass