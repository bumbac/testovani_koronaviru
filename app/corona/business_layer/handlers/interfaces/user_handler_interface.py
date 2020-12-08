from abc import ABC, abstractmethod

"""
Interface of UserHandler
"""
class UserHandlerInterface(ABC):
    @abstractmethod
    def create_user(self, username, password):
        """
        :param username: User's username
        :param password: User's password
        :return: True if successful, otherwise False
        """
        pass

    @abstractmethod
    def check_password(self, username, password):
        """
        Method checks, if the password passed in a form matches the one in the database
        :param username: User's username
        :param password: User's password
        :return: True if successful, otherwise False
        """
        pass
