from abc import ABC, abstractmethod


class UserDataAccessInterface(ABC):
    @abstractmethod
    def add_user(self, username, password):
        pass

    @abstractmethod
    def edit_user(self, username):
        pass

    @abstractmethod
    def get_user(self, username):
        pass
