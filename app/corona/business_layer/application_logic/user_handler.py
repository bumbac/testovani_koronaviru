from corona.business_layer.application_logic.interfaces.user_handler_interface import UserHandlerInterface
from corona.data_layer.user_data_access import UserDataAccess


class UserHandler(UserHandlerInterface):
    def create_user(self, username, password):
        user_data_access = UserDataAccess()
        user_data_access.add_user(username=username, password=password)

    def check_password(self, username, password):
        pass