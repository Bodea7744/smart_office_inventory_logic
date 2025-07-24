# Staff Roles – Base + Contract + Freelance

from entity_base import Entity
from datetime import datetime

class Staff(Entity):
    def __init__(self, name, email, address, salary, working_hours):
        super().__init__(name, email, address)
        self.__salary = salary
        self._working_hours = working_hours

    def increase_salary(self, percentage):
        self.__salary += self.__salary * percentage / 100

    def checkin(self):
        self._start_time = datetime.now()

    def checkout(self):
        self._end_time = datetime.now()
        duration = (self._end_time - self._start_time).total_seconds() / 3600
        self._working_hours += round(duration, 2)

    def get_salary(self):
        return self.__salary

    def get_working_hours(self):
        return self._working_hours

    def display_info(self):
        print(f"Name: {self.name}, Email: {self._email}, Salary: {self.__salary}, Hours: {self._working_hours}")

class ContractStaff(Staff):
    def __init__(self, name, email, address, salary, working_hours, contract_expiry):
        super().__init__(name, email, address, salary, working_hours)
        self.contract_expiry = contract_expiry

    def display_info(self):
        print(f"{self.name} – Contract until {self.contract_expiry}, Hours: {self.get_working_hours()}")

class FreelanceStaff(Staff):
    def __init__(self, name, email, address, salary, working_hours, project_count):
        super().__init__(name, email, address, salary, working_hours)
        self.project_count = project_count

    def display_info(self):
        print(f"{self.name} – {self.project_count} active projects, Hours: {self.get_working_hours()}")