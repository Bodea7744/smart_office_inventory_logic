# Abstract Base Class – Entity (Staff / User)

from abc import ABC, abstractmethod

class Entity(ABC):
    def __init__(self, name, email, address):
        self.name = name
        self._email = email
        self.__password = ""
        self._address = address
        self.__login_status = False

    def check_email(self):
        return "@" in self._email

    def set_password(self, password):
        self.__password = password

    def check_login(self, email, password):
        if self._email == email and self.__password == password:
            self.__login_status = True
            return True
        return False

    @abstractmethod
    def display_info(self):
        pass