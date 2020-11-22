from corona.business_layer.application_logic.interfaces.patient_handler_interface import PatientHandlerInterface
from corona.data_layer.patient_data_access import PatientDataAccess


class PatientHandler(PatientHandlerInterface):
    def create_patient(self, name, surname, birthid, email, phone, address, user):
        patient_data_access = PatientDataAccess()
        patient_data_access.add_patient(name=name, surname=surname, birthid=birthid, email=email, phone=phone, address=address, user=user)