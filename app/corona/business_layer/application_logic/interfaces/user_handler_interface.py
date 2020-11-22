from abc import ABC, abstractmethod


class UserHandlerInterface(ABC):
    @abstractmethod
    def create_user(self, username, password):
        pass

    @abstractmethod
    def check_password(self, username, password):
        pass
