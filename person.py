
from abc import ABC, abstractmethod

class Person(ABC):
    def __init__(self, name, email, address, password):
        self.name = name
        self._email = email  # Protejat
        self.__password = password  # Privat
        self._address = address  # Protejat
        self.__login = False  # Privat

    def check_email(self):
        return '@' in self._email

    def check_login(self, email, password):
        if self._email == email and self.__password == password:
            self.__login = True
            return True
        return False

    def get_email(self):
        return self._email

    def set_email(self, email):
        self._email = email

    def get_address(self):
        return self._address

    def set_address(self, address):
        self._address = address

    @abstractmethod
    def display_info(self):
        pass
