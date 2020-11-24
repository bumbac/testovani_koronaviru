from abc import ABC, abstractmethod


class CovidtestDataAccessInterface(ABC):
    @abstractmethod
    def add_covidtest(self, waitdays, price, type):
        pass

    @abstractmethod
    def get_covidtest(self, type):
        pass