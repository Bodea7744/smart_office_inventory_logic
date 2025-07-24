# WorkspaceUser Class – Internal Platform User

from person_base import Person

class WorkspaceUser(Person):
    def __init__(self, name, email, address, phone, access_log: list):
        super().__init__(name, email, address)
        self.phone = phone
        self.access_log = access_log

    def get_phone(self):
        return self.phone

    def set_phone(self, phone):
        self.phone = phone

    def add_equipment(self, price):
        self.access_log.append(price)

    def total_spent(self):
        return sum(self.access_log)

    def display_info(self):
        return (
            f"Name: {self.name}\n"
            f"Email: {self.get_email()}\n"
            f"Address: {self.get_address()}\n"
            f"Phone: {self.phone}\n"
            f"Total spent: {self.total_spent()} RON"
        )